"""Report runner that generates output directly to a file."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

from app.reports.contracts import ReportContext, ReportDefinition, ReportResult
from app.reports.schemas import ReportParams


class ReportRunner:
    def __init__(self, context: ReportContext):
        self._context = context

    def run(self, report: ReportDefinition, params: ReportParams) -> ReportResult:
        writer = report.output_writer()
        out_dir = Path(self._context.settings.reports_output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_id = report.id.replace(".", "_")
        output_path = out_dir / f"{safe_id}_{ts}{writer.extension}"

        warnings = report.generate_to_file(params=params, context=self._context, output_path=output_path)
        return ReportResult(output_file_path=output_path, mime_type=writer.mime_type, warnings=warnings)
