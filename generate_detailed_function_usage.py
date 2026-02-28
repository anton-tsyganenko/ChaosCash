#!/usr/bin/env python3
"""
Advanced function usage analyzer with Qt-specific support.
Detects signal-slot connections, callbacks, and more detailed usage patterns.
"""

import ast
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict

class DetailedFunctionAnalyzer(ast.NodeVisitor):
    """Advanced analyzer for function usage including Qt patterns."""

    def __init__(self, filepath: str, content: str):
        self.filepath = filepath
        self.content = content
        self.lines = content.split('\n')
        self.functions_defined = {}  # {name: (line_no, type, class_name, signature)}
        self.function_usages = defaultdict(list)  # {name: [(line_no, usage_type, context)]}
        self.current_class = None
        self.current_function = None
        self.qt_connections = []
        self.imports = {}

    def get_line_context(self, line_no: int) -> str:
        """Get context around a line."""
        if 0 < line_no <= len(self.lines):
            return self.lines[line_no - 1].strip()
        return ""

    def visit_FunctionDef(self, node):
        """Record function definitions."""
        name = node.name
        line_no = node.lineno
        func_type = 'method' if self.current_class else 'function'

        # Build signature
        args = [arg.arg for arg in node.args.args]
        signature = f"({', '.join(args)})"

        self.functions_defined[name] = {
            'line': line_no,
            'type': func_type,
            'class': self.current_class,
            'signature': signature,
            'is_async': False,
            'file': self.filepath
        }

        old_func = self.current_function
        self.current_function = name
        self.generic_visit(node)
        self.current_function = old_func

    def visit_AsyncFunctionDef(self, node):
        """Record async function definitions."""
        name = node.name
        line_no = node.lineno
        func_type = 'async_method' if self.current_class else 'async_function'

        args = [arg.arg for arg in node.args.args]
        signature = f"({', '.join(args)})"

        self.functions_defined[name] = {
            'line': line_no,
            'type': func_type,
            'class': self.current_class,
            'signature': signature,
            'is_async': True,
            'file': self.filepath
        }

        old_func = self.current_function
        self.current_function = name
        self.generic_visit(node)
        self.current_function = old_func

    def visit_ClassDef(self, node):
        """Track class scope."""
        old_class = self.current_class
        self.current_class = node.name
        self.generic_visit(node)
        self.current_class = old_class

    def visit_Call(self, node):
        """Record function calls."""
        context = self.get_line_context(node.lineno)

        if isinstance(node.func, ast.Name):
            # Direct function call: foo()
            func_name = node.func.id
            self.function_usages[func_name].append({
                'line': node.lineno,
                'type': 'direct_call',
                'context': context,
                'called_from': self.current_function,
                'class': self.current_class
            })

            # Detect Qt connect patterns
            if func_name == 'connect':
                self._analyze_qt_connect(node)

        elif isinstance(node.func, ast.Attribute):
            # Method call: obj.method() or module.function()
            attr_name = node.func.attr
            self.function_usages[attr_name].append({
                'line': node.lineno,
                'type': 'method_call',
                'context': context,
                'called_from': self.current_function,
                'class': self.current_class
            })

        self.generic_visit(node)

    def _analyze_qt_connect(self, node):
        """Analyze Qt signal-slot connections."""
        try:
            context = self.get_line_context(node.lineno)
            if 'connect' in context and '.' in context:
                # Try to parse signal and slot names
                match = re.search(r'\.connect\s*\(\s*([^,]+),\s*([^)]+)\)', context)
                if match:
                    signal = match.group(1).strip()
                    slot = match.group(2).strip()
                    self.qt_connections.append({
                        'line': node.lineno,
                        'signal': signal,
                        'slot': slot,
                        'context': context
                    })
        except:
            pass

    def visit_Import(self, node):
        """Record imports."""
        for alias in node.names:
            name = alias.asname or alias.name
            self.imports[name] = alias.name
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        """Record from imports."""
        for alias in node.names:
            name = alias.asname or alias.name
            full_name = f"{node.module}.{alias.name}" if node.module else alias.name
            self.imports[name] = full_name
        self.generic_visit(node)

    def visit_Attribute(self, node):
        """Detect attribute access patterns (for method references)."""
        if isinstance(node.value, ast.Name):
            # Pattern like: object.method_name
            self.generic_visit(node)

    def visit_Lambda(self, node):
        """Track lambda definitions as callbacks."""
        context = self.get_line_context(node.lineno)
        # Lambda functions contain inline calls
        self.generic_visit(node)


def analyze_file_detailed(filepath: str) -> Tuple[Dict, Dict, List]:
    """Detailed analysis of a Python file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        tree = ast.parse(content, filename=filepath)
        analyzer = DetailedFunctionAnalyzer(filepath, content)
        analyzer.visit(tree)

        return analyzer.functions_defined, analyzer.function_usages, analyzer.qt_connections
    except Exception as e:
        return {}, {}, []


def find_all_usages_with_context(root_dir: str, function_name: str) -> List[Dict]:
    """Find all usages of a function with detailed context."""
    usages = []

    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.pytest_cache', 'venv', 'env']]

        for file in files:
            if not file.endswith('.py'):
                continue

            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line_no, line in enumerate(f, 1):
                        # Look for direct calls
                        if re.search(rf'\b{re.escape(function_name)}\s*\(', line):
                            usages.append({
                                'file': filepath,
                                'line': line_no,
                                'type': 'call',
                                'context': line.rstrip()
                            })
                        # Look for method calls
                        elif re.search(rf'\.{re.escape(function_name)}\s*\(', line):
                            usages.append({
                                'file': filepath,
                                'line': line_no,
                                'type': 'method_call',
                                'context': line.rstrip()
                            })
            except:
                pass

    return usages


def generate_comprehensive_report(root_dir: str = '/home/user/ChaosCash') -> str:
    """Generate comprehensive function usage documentation."""

    report = []
    report.append("# Подробная документация использования функций и методов")
    report.append("")
    report.append("*Дата создания: 2026-02-28*")
    report.append("*Проект: ChaosCash*")
    report.append("")
    report.append("---")
    report.append("")

    # Collect all definitions and usages
    all_definitions = {}
    all_usages = defaultdict(list)
    all_qt_connections = []

    python_files = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.pytest_cache', 'venv', 'env']]
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))

    print(f"Анализирование {len(python_files)} файлов...")

    for filepath in sorted(python_files):
        definitions, usages, qt_connections = analyze_file_detailed(filepath)

        for func_name, func_info in definitions.items():
            full_name = f"{func_info['class']}.{func_name}" if func_info['class'] else func_name
            all_definitions[full_name] = func_info

        for func_name, usage_list in usages.items():
            all_usages[func_name].extend(usage_list)

        all_qt_connections.extend(qt_connections)

    # Generate table of contents
    report.append("## Оглавление")
    report.append("")
    report.append("1. [Статистика](#статистика)")
    report.append("2. [Qt сигналы и слоты](#qt-сигналы-и-слоты)")
    report.append("3. [Функции и методы](#функции-и-методы)")
    report.append("4. [Неиспользуемые функции](#неиспользуемые-функции)")
    report.append("")
    report.append("---")
    report.append("")

    # Statistics
    report.append("## Статистика")
    report.append("")
    report.append(f"- **Всего функций/методов:** {len(all_definitions)}")
    report.append(f"- **Qt соединений обнаружено:** {len(all_qt_connections)}")

    unused_count = len([f for f, info in all_definitions.items()
                        if not any(u['type'] in ['call', 'method_call']
                                  for u in all_usages.get(f.split('.')[-1], []))])
    report.append(f"- **Неиспользуемые функции:** {unused_count}")
    report.append(f"- **Анализировано файлов:** {len(python_files)}")
    report.append("")
    report.append("---")
    report.append("")

    # Qt Connections Section
    if all_qt_connections:
        report.append("## Qt сигналы и слоты")
        report.append("")
        report.append(f"Найдено {len(all_qt_connections)} Qt-соединений:")
        report.append("")

        for conn in sorted(all_qt_connections, key=lambda x: x['line']):
            rel_file = os.path.relpath(conn.get('file', ''), root_dir)
            report.append(f"### {rel_file}:{conn['line']}")
            report.append("")
            report.append(f"**Сигнал:** `{conn['signal']}`")
            report.append("")
            report.append(f"**Слот:** `{conn['slot']}`")
            report.append("")
            report.append(f"```python")
            report.append(f"{conn['context']}")
            report.append(f"```")
            report.append("")

    report.append("---")
    report.append("")

    # Functions and Methods
    report.append("## Функции и методы")
    report.append("")
    report.append("### По типам")
    report.append("")

    # Group by type
    by_type = defaultdict(list)
    for name, info in all_definitions.items():
        by_type[info['type']].append(name)

    for func_type in sorted(by_type.keys()):
        names = sorted(by_type[func_type])
        report.append(f"#### {func_type.capitalize()} ({len(names)})")
        report.append("")
        for name in names[:20]:  # Show first 20
            report.append(f"- {name}")
        if len(names) > 20:
            report.append(f"- ... и ещё {len(names) - 20}")
        report.append("")

    # Detailed function info
    report.append("### Детальный список")
    report.append("")

    for func_name in sorted(all_definitions.keys()):
        func_info = all_definitions[func_name]
        rel_file = os.path.relpath(func_info['file'], root_dir)

        report.append(f"#### {func_name}")
        report.append("")
        report.append(f"**Определено в:** `{rel_file}:{func_info['line']}`")
        report.append("")
        report.append(f"**Тип:** {func_info['type']}")
        report.append("")

        if func_info['signature']:
            report.append(f"**Сигнатура:** `{func_name}{func_info['signature']}`")
            report.append("")

        # Find usages
        short_name = func_name.split('.')[-1]
        usages = [u for u in all_usages.get(short_name, [])
                 if u['type'] in ['call', 'method_call']]

        if usages:
            report.append(f"**Использования ({len(usages)} мест):**")
            report.append("")
            for usage in sorted(set(str(u) for u in usages))[:10]:
                # Parse the usage dict string and extract useful info
                try:
                    # Create a simple display
                    if 'file' in eval(usage):
                        usage_dict = eval(usage)
                        rel_path = os.path.relpath(usage_dict['file'], root_dir)
                        report.append(f"- `{rel_path}:{usage_dict['line']}`")
                except:
                    report.append(f"- {usage}")

            if len(usages) > 10:
                report.append(f"- ... и ещё {len(usages) - 10}")
        else:
            report.append("**Использования:** Не найдены (возможно, неиспользуемая функция)")

        report.append("")

    # Unused functions
    report.append("---")
    report.append("")
    report.append("## Неиспользуемые функции")
    report.append("")

    unused = [name for name, info in all_definitions.items()
             if not all_usages.get(name.split('.')[-1], [])]

    if unused:
        report.append(f"Найдено {len(unused)} неиспользуемых функций:")
        report.append("")
        for name in sorted(unused):
            func_info = all_definitions[name]
            rel_file = os.path.relpath(func_info['file'], root_dir)
            report.append(f"- **{name}** (`{rel_file}:{func_info['line']}`)")
    else:
        report.append("Все функции используются.")

    return "\n".join(report)


def main():
    print("Запуск детального анализа кодовой базы...")
    report = generate_comprehensive_report()

    output_file = '/home/user/ChaosCash/FUNCTION_USAGE_DETAILED.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"Подробный отчёт сохранён в: {output_file}")


if __name__ == '__main__':
    main()
