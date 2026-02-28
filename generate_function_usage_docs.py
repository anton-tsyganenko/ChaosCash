#!/usr/bin/env python3
"""
Analyze Python codebase and document function/method usage.
Generates a comprehensive report of all functions/methods and their usage locations.
"""

import ast
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict

class FunctionUsageAnalyzer(ast.NodeVisitor):
    """Analyzes function and method definitions and their usage."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.definitions = {}  # {name: (line_no, type, class_name)}
        self.usages = defaultdict(list)  # {name: [(line_no, context)]}
        self.current_class = None
        self.imports = {}  # {name: module}

    def visit_FunctionDef(self, node):
        """Record function definitions."""
        name = node.name
        line_no = node.lineno
        func_type = 'method' if self.current_class else 'function'
        class_name = self.current_class

        self.definitions[name] = (line_no, func_type, class_name)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        """Record async function definitions."""
        name = node.name
        line_no = node.lineno
        func_type = 'async_method' if self.current_class else 'async_function'
        class_name = self.current_class

        self.definitions[name] = (line_no, func_type, class_name)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        """Track class scope for methods."""
        old_class = self.current_class
        self.current_class = node.name
        self.generic_visit(node)
        self.current_class = old_class

    def visit_Call(self, node):
        """Record function/method calls."""
        if isinstance(node.func, ast.Name):
            # Direct function call: foo()
            self.usages[node.func.id].append((node.lineno, 'call'))
        elif isinstance(node.func, ast.Attribute):
            # Method call: obj.method()
            self.usages[node.func.attr].append((node.lineno, 'method_call'))

        self.generic_visit(node)

    def visit_Import(self, node):
        """Record imports."""
        for alias in node.names:
            self.imports[alias.asname or alias.name] = alias.name
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        """Record from imports."""
        for alias in node.names:
            name = alias.asname or alias.name
            self.imports[name] = f"{node.module}.{alias.name}"
        self.generic_visit(node)


def analyze_file(filepath: str) -> Tuple[Dict, Dict]:
    """Analyze a Python file for function definitions and usage."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        tree = ast.parse(content, filename=filepath)
        analyzer = FunctionUsageAnalyzer(filepath)
        analyzer.visit(tree)

        return analyzer.definitions, analyzer.usages
    except SyntaxError as e:
        print(f"Warning: Syntax error in {filepath}: {e}")
        return {}, {}
    except Exception as e:
        print(f"Warning: Error analyzing {filepath}: {e}")
        return {}, {}


def search_usages_in_file(filepath: str, function_name: str) -> List[Tuple[int, str]]:
    """
    Search for usages of a function in a file using regex.
    Returns list of (line_no, line_content).
    """
    usages = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line_no, line in enumerate(f, 1):
                # Skip comments
                if line.strip().startswith('#'):
                    continue

                # Look for function calls
                pattern = rf'\b{re.escape(function_name)}\s*\('
                if re.search(pattern, line):
                    usages.append((line_no, line.rstrip()))

                # Look for attribute access (.method)
                pattern = rf'\.{re.escape(function_name)}\s*\('
                if re.search(pattern, line):
                    usages.append((line_no, line.rstrip()))

    except Exception as e:
        pass

    return usages


def analyze_codebase(root_dir: str = '/home/user/ChaosCash') -> Dict:
    """Analyze entire codebase and generate usage report."""

    results = {
        'functions': {},  # {name: {'defined_in': ..., 'usages': [...]}}
        'files': {}
    }

    # Collect all function definitions
    all_definitions = {}  # {(filepath, name): (line_no, type, class_name)}

    python_files = []
    for root, dirs, files in os.walk(root_dir):
        # Skip common non-essential directories
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.pytest_cache', 'venv', 'env']]

        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))

    # First pass: collect all definitions
    for filepath in python_files:
        definitions, _ = analyze_file(filepath)
        results['files'][filepath] = {'definitions': definitions}

        for func_name, (line_no, func_type, class_name) in definitions.items():
            key = (filepath, func_name, class_name)
            all_definitions[key] = line_no

    # Second pass: find all usages
    usages_by_name = defaultdict(list)

    for filepath in python_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                content = f.read()
                tree = ast.parse(content, filename=filepath)

                # Use AST to find calls
                for node in ast.walk(tree):
                    if isinstance(node, ast.Call):
                        if isinstance(node.func, ast.Name):
                            usages_by_name[node.func.id].append((filepath, node.lineno))
                        elif isinstance(node.func, ast.Attribute):
                            usages_by_name[node.func.attr].append((filepath, node.lineno))
            except:
                pass

    # Compile results
    for (filepath, func_name, class_name), line_no in all_definitions.items():
        full_name = f"{class_name}.{func_name}" if class_name else func_name

        if full_name not in results['functions']:
            results['functions'][full_name] = {
                'defined_in': f"{filepath}:{line_no}",
                'class': class_name,
                'usages': []
            }

        # Find all usages of this function
        for file_path, line in usages_by_name[func_name]:
            rel_path = os.path.relpath(file_path, root_dir)
            results['functions'][full_name]['usages'].append(f"{file_path}:{line}")

    return results


def generate_markdown_report(results: Dict) -> str:
    """Generate markdown documentation from analysis results."""

    report = ["# Документация использования функций и методов\n"]
    report.append(f"Дата создания: 2026-02-28\n")
    report.append(f"Всего функций/методов: {len(results['functions'])}\n\n")

    report.append("## Индекс функций\n\n")

    # Sort by name
    for func_name in sorted(results['functions'].keys()):
        report.append(f"- [{func_name}](#{func_name.replace('.', '-').replace('_', '-').lower()})\n")

    report.append("\n---\n\n")

    # Detailed listing
    report.append("## Подробный список\n\n")

    for func_name in sorted(results['functions'].keys()):
        func_info = results['functions'][func_name]
        report.append(f"### {func_name}\n\n")
        report.append(f"**Определено в:** `{func_info['defined_in']}`\n\n")

        if func_info['class']:
            report.append(f"**Тип:** Метод класса `{func_info['class']}`\n\n")
        else:
            report.append(f"**Тип:** Функция\n\n")

        usages = func_info['usages']
        if usages:
            report.append(f"**Использования ({len(usages)} мест):**\n\n")
            for usage in sorted(set(usages)):
                report.append(f"- `{usage}`\n")
        else:
            report.append(f"**Использования:** Нет (возможно, неиспользуемая функция)\n")

        report.append("\n")

    return "".join(report)


def main():
    print("Анализирование кодовой базы...")
    results = analyze_codebase()

    print(f"Найдено функций/методов: {len(results['functions'])}")

    # Generate markdown report
    report = generate_markdown_report(results)

    # Save to file
    output_file = '/home/user/ChaosCash/FUNCTION_USAGE.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"Отчёт сохранён в: {output_file}")

    # Print summary
    print("\n=== Краткая статистика ===")
    unused = [name for name, info in results['functions'].items() if not info['usages']]
    print(f"Неиспользуемые функции: {len(unused)}")
    if unused:
        for func in sorted(unused)[:10]:
            print(f"  - {func}")
        if len(unused) > 10:
            print(f"  ... и ещё {len(unused) - 10}")


if __name__ == '__main__':
    main()
