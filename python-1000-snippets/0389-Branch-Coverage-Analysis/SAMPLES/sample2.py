# sample2.py
# Runs the core logic under a `coverage` run and prints a branch coverage summary.

import os


def run_branch_coverage() -> None:
    """Run the `check_value` function while collecting branch coverage."""

    try:
        import coverage  # type: ignore
    except ImportError:  # pragma: no cover
        print("coverage not installed; install with `pip install coverage`")
        return

    # Use a temp file for the coverage data to avoid side effects in the repo.
    data_file = os.path.join(os.path.dirname(__file__), ".coverage.branch")
    cov = coverage.Coverage(data_file=data_file, branch=True)

    # Start coverage measurement before importing the target module.
    cov.start()

    # Import is intentionally done after coverage starts so that the module is measured.
    import sample1  # type: ignore

    # Exercise the branches.
    for value in (-1, 0, 1):
        sample1.check_value(value)

    cov.stop()
    cov.save()

    # Print a simple console coverage report.
    cov.report(show_missing=True, skip_empty=True)


if __name__ == "__main__":
    run_branch_coverage()
