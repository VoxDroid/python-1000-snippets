# 0389-Branch-Coverage-Analysis Cheatsheet

- **Branch coverage** checks that each conditional branch (e.g., `if/else`) is executed at least once.
- To collect branch coverage from the command line:
  - `coverage run --branch -m pytest`
  - `coverage report -m`
  - `coverage html`
- To collect branch coverage programmatically (as in this snippet):
  - `coverage.Coverage(branch=True)`
  - `cov.start()` / `cov.stop()` / `cov.save()`
  - `cov.report(show_missing=True)`
  - `cov.html_report(directory=...)`
- Run examples:
  - `python SAMPLES/sample1.py` — runs branchy logic.
  - `python SAMPLES/sample2.py` — prints a branch coverage summary (requires `coverage`).
  - `python SAMPLES/sample3.py` — generates an HTML report.
