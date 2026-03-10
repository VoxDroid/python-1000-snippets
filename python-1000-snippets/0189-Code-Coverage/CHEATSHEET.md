# 0189-Code-Coverage Cheatsheet

* **Install tools**: `sudo apt-get install python3-coverage` or `pip install coverage pytest-cov`
* **Run with pytest plugin**: `pytest --cov=module test_*.py`
* **Run via coverage CLI**:
  ```bash
  coverage run -m pytest
  coverage report -m
  coverage html      # generate HTML report in htmlcov/
  ```
* **Programmatic API**:
  ```python
  import coverage
  cov = coverage.Coverage()
  cov.start()
  # run tests or code
  cov.stop(); cov.save()
  cov.report()        # or cov.html_report()
  ```
* **Exclude files** using `.coveragerc` or `--omit`/`--include` options.
* **Combine data** from multiple runs: `coverage combine` then `coverage report`.
* **Interpretation**: coverage <100% indicates untested lines; add tests accordingly.

