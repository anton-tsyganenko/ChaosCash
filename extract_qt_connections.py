#!/usr/bin/env python3
"""
Extract and document PyQt signal-slot connections.
"""

import re
import os
from pathlib import Path
from typing import List, Dict
from collections import defaultdict

def extract_qt_connections(root_dir: str = '/home/user/ChaosCash') -> Dict[str, List[Dict]]:
    """Extract all PyQt signal-slot connections from codebase."""

    connections = defaultdict(list)
    signal_patterns = [
        # Pattern 1: signal.connect(method)
        r'(\w+(?:\.\w+)*)\s*\.connect\s*\(\s*(\w+(?:\.\w+)*)\s*\)',
        # Pattern 2: obj.signal.connect(callback)
        r'(\w+(?:\.\w+)*)\s*\.connect\s*\(\s*lambda.*?\)',
    ]

    qt_signal_names = [
        'clicked', 'pressed', 'released', 'toggled',
        'text_changed', 'textChanged', 'currentIndexChanged',
        'itemSelectionChanged', 'itemDoubleClicked', 'itemClicked',
        'cellDoubleClicked', 'cellClicked', 'cellChanged',
        'itemExpanded', 'itemCollapsed',
        'accepted', 'rejected', 'finished',
        'value_changed', 'valueChanged',
        'returnPressed', 'editingFinished',
        'customContextMenuRequested',
        'selection_changed', 'selectionChanged',
        'doubleClicked', 'activated', 'highlighted',
    ]

    python_files = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.pytest_cache', 'venv', 'env']]
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))

    print(f"Анализирование {len(python_files)} файлов на наличие Qt-соединений...")

    for filepath in sorted(python_files):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            for line_no, line in enumerate(lines, 1):
                # Skip comments
                if line.strip().startswith('#'):
                    continue

                # Look for .connect patterns
                if '.connect(' in line:
                    match = re.search(r'(\w+(?:\.\w+)*)\s*\.connect\s*\(\s*([^)]+)\)', line)
                    if match:
                        signal = match.group(1).strip()
                        slot = match.group(2).strip()

                        # Get surrounding context (previous and next lines)
                        context_start = max(0, line_no - 2)
                        context_end = min(len(lines), line_no + 1)
                        context = ''.join(lines[context_start:context_end])

                        connections[filepath].append({
                            'line': line_no,
                            'signal': signal,
                            'slot': slot,
                            'full_line': line.rstrip(),
                            'context': context.rstrip(),
                            'type': 'connect'
                        })

                # Look for lambda callbacks
                if 'lambda' in line and '(' in line:
                    match = re.search(r'(\w+(?:\.\w+)*)\s*\.(\w+)\s*\(.*?lambda.*?\)', line)
                    if match:
                        obj = match.group(1)
                        method = match.group(2)
                        connections[filepath].append({
                            'line': line_no,
                            'signal': f"{obj}.{method}",
                            'slot': 'lambda',
                            'full_line': line.rstrip(),
                            'context': line.rstrip(),
                            'type': 'lambda'
                        })

        except Exception as e:
            pass

    return dict(connections)


def extract_pyqt_decorators(root_dir: str = '/home/user/ChaosCash') -> Dict[str, List[Dict]]:
    """Extract PyQt slot decorators and other decorators."""

    decorators = defaultdict(list)
    decorator_patterns = [
        (r'@pyqtSlot\s*\((.*?)\)', 'pyqtSlot'),
        (r'@Slot\s*\((.*?)\)', 'Slot'),
        (r'@Signal\s*\((.*?)\)', 'Signal'),
    ]

    python_files = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.pytest_cache', 'venv', 'env']]
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))

    print(f"Анализирование {len(python_files)} файлов на наличие PyQt-декораторов...")

    for filepath in sorted(python_files):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')

            for i, line in enumerate(lines, 1):
                for pattern, decorator_type in decorator_patterns:
                    if re.search(pattern, line):
                        match = re.search(pattern, line)
                        if match:
                            params = match.group(1) if match.lastindex else ''
                            # Find the decorated function
                            next_line_idx = i
                            if next_line_idx < len(lines):
                                next_line = lines[next_line_idx].strip()
                                func_match = re.search(r'def\s+(\w+)\s*\(', next_line)
                                func_name = func_match.group(1) if func_match else 'unknown'
                            else:
                                func_name = 'unknown'

                            decorators[filepath].append({
                                'line': i,
                                'decorator': decorator_type,
                                'params': params,
                                'function': func_name,
                                'full_line': line.rstrip()
                            })

        except Exception as e:
            pass

    return dict(decorators)


def generate_qt_report(root_dir: str = '/home/user/ChaosCash') -> str:
    """Generate report on PyQt connections and decorators."""

    report = []
    report.append("# PyQt Сигналы, Слоты и Соединения")
    report.append("")
    report.append("*Дата создания: 2026-02-28*")
    report.append("")

    # Extract connections
    connections = extract_qt_connections(root_dir)
    decorators = extract_pyqt_decorators(root_dir)

    # Statistics
    total_connections = sum(len(v) for v in connections.values())
    total_decorators = sum(len(v) for v in decorators.values())

    report.append("## Статистика")
    report.append("")
    report.append(f"- **Найдено .connect() соединений:** {total_connections}")
    report.append(f"- **Найдено PyQt-декораторов:** {total_decorators}")
    report.append(f"- **Файлов с соединениями:** {len(connections)}")
    report.append(f"- **Файлов с декораторами:** {len(decorators)}")
    report.append("")

    # Signal-Slot Connections
    report.append("## Signal-Slot соединения (.connect)")
    report.append("")

    if connections:
        for filepath in sorted(connections.keys()):
            rel_path = os.path.relpath(filepath, root_dir)
            file_connections = connections[filepath]

            report.append(f"### {rel_path}")
            report.append("")
            report.append(f"Соединений: {len(file_connections)}")
            report.append("")

            for conn in file_connections:
                report.append(f"**Строка {conn['line']}:**")
                report.append("")
                report.append(f"- **Сигнал:** `{conn['signal']}`")
                report.append(f"- **Слот:** `{conn['slot']}`")
                report.append(f"- **Тип:** {conn['type']}")
                report.append("")
                report.append(f"```python")
                report.append(f"{conn['full_line']}")
                report.append(f"```")
                report.append("")
    else:
        report.append("Соединений не найдено.")
        report.append("")

    # Decorators
    report.append("---")
    report.append("")
    report.append("## PyQt Декораторы (@pyqtSlot, @Slot, @Signal)")
    report.append("")

    if decorators:
        for filepath in sorted(decorators.keys()):
            rel_path = os.path.relpath(filepath, root_dir)
            file_decorators = decorators[filepath]

            report.append(f"### {rel_path}")
            report.append("")
            report.append(f"Декораторов: {len(file_decorators)}")
            report.append("")

            for dec in file_decorators:
                report.append(f"**Строка {dec['line']}:**")
                report.append("")
                report.append(f"- **Тип:** `{dec['decorator']}`")
                report.append(f"- **Функция:** `{dec['function']}`")
                if dec['params']:
                    report.append(f"- **Параметры:** `{dec['params']}`")
                report.append("")
                report.append(f"```python")
                report.append(f"{dec['full_line']}")
                report.append(f"```")
                report.append("")
    else:
        report.append("PyQt-декораторы не найдены.")
        report.append("")

    # Summary of commonly connected signals
    report.append("---")
    report.append("")
    report.append("## Анализ часто используемых сигналов")
    report.append("")

    signal_counts = defaultdict(int)
    for file_conns in connections.values():
        for conn in file_conns:
            signal = conn['signal'].split('.')[-1]
            signal_counts[signal] += 1

    if signal_counts:
        report.append("### Самые часто используемые сигналы:")
        report.append("")
        for signal, count in sorted(signal_counts.items(), key=lambda x: -x[1])[:15]:
            report.append(f"- `{signal}` — {count} использований")
    else:
        report.append("Сигналы не найдены.")

    report.append("")

    return "\n".join(report)


def main():
    report = generate_qt_report()

    output_file = '/home/user/ChaosCash/QT_CONNECTIONS.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"Отчёт о Qt-соединениях сохранён в: {output_file}")


if __name__ == '__main__':
    main()
