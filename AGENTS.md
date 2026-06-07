# ChaosCash — AGENTS.md

## Run

```sh
python main.py [path/to/file.ccash]
python main.py --debug-logging     # detailed UI/model/sql logs
```

## Test

```sh
python -m pytest      # all tests (in-memory SQLite, no config)
```

## Deps

Only `PyQt6>=6.4.0` and `pytest>=7.0.0` in `requirements.txt`. No pyproject.toml, no packaging.

## Lint / format

Ruff has been used historically but no config committed. Run manually:
```sh
ruff check . && ruff format .
```

No CI, no pre-commit, no Docker.

## Architecture

```
main.py → MainWindow (app/ui/main_window.py)
  ├── Repositories (app/repositories/) — raw SQL via app/database/queries/
  ├── Services    (app/services/)       — business logic
  └── Qt Model/View:
        ├── item_models/   — QAbstractTableModel subclasses
        ├── widgets/       — QTableView subclasses
        └── delegates/     — custom cell editors
```

Entrypoint: `main.py`. No packaging — `sys.path.insert(0, ...)` for imports.

Database: SQLite with WAL mode, foreign keys enforced. Schema in `app/database/schema.py`. DB files use `.ccash` or `.db` extension.

UI event logger in `app/ui/ui_event_logger.py` — logs click/target/accept info when `--debug-logging` is on.

## i18n

All user-visible strings go through `app.i18n.tr()`. Translations are JSON files in `translations/<lang>.json`. Report plugins have their own `<lang>.json` alongside `__init__.py`.

## Reports

Plugin-based. Add a new report in `app/reports/plugins/<name>/__init__.py` implementing `ReportDefinition` protocol. Parameter schema defined via `ReportParameterSchema` fields.

## Code style

- No trailing comments in code (user preference)
- Imports sorted with ruff (see commit `1478760`)
- Use `AmountFormatter` (not raw string formatting) for monetary values
