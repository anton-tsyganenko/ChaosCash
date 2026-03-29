from dataclasses import dataclass
from pathlib import Path

from app.reports.contracts import OutputWriterSpec
from app.reports.runner import ReportRunner
from app.reports.schemas import ReportParameterSchema, ReportParams


class DummyReport:
    id = "dummy.report"
    title = "Dummy"

    def parameter_schema(self):
        return ReportParameterSchema(fields=[])

    def output_writer(self):
        return OutputWriterSpec(extension=".txt", mime_type="text/plain")

    def generate_to_file(self, params, context, output_path: Path):
        output_path.write_text("ok", encoding="utf-8")
        return []


@dataclass(frozen=True)
class DummyContext:
    settings: object


@dataclass(frozen=True)
class DummySettings:
    reports_output_dir: str


def test_report_runner_writes_file(tmp_path):
    settings = DummySettings(reports_output_dir=str(tmp_path))
    context = DummyContext(settings=settings)
    runner = ReportRunner(context)  # type: ignore[arg-type]

    result = runner.run(DummyReport(), ReportParams(values={}))

    assert result.output_file_path.exists()
    assert result.output_file_path.read_text(encoding="utf-8") == "ok"
    assert result.mime_type == "text/plain"
