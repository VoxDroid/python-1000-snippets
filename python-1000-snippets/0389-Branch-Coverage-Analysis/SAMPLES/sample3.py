# sample3.py
# Runs branch coverage and generates an HTML report.

import os
import tempfile


def run_html_coverage_report() -> None:
    try:
        import coverage  # type: ignore
    except ImportError:  # pragma: no cover
        print("coverage not installed; install with `pip install coverage`")
        return

    # Create a temporary directory for the HTML report.
    with tempfile.TemporaryDirectory(prefix="branch_coverage_") as tmpdir:
        data_file = os.path.join(tmpdir, ".coverage")
        cov = coverage.Coverage(data_file=data_file, branch=True)
        cov.start()

        # Import and exercise the code under coverage.
        import sample1  # type: ignore
        for value in (-1, 0, 1):
            sample1.check_value(value)

        cov.stop()
        cov.save()

        html_dir = os.path.join(tmpdir, "htmlcov")
        cov.html_report(directory=html_dir)

        print("HTML coverage report generated:")
        print(html_dir)
        print("Open index.html in a browser to view branch coverage details.")


if __name__ == "__main__":
    run_html_coverage_report()
