# 0188-Pytest-Setup Cheatsheet

* Install pytest: `sudo apt-get install python3-pytest` or `pip install pytest`
* Run tests in a directory: `pytest` (discovers `test_*.py` or `*_test.py`).
* Run a single file: `pytest path/to/file.py`.
* Verbose output: `pytest -v`; show assertions: `-vv`.
* Use markers: `@pytest.mark.slow` and run subset with `-m slow`.
* Fixtures:
  ```python
  @pytest.fixture
  def resource():
      return setup()
  def test_use(resource):
      assert resource.do_something()
  ```
* Parametrized tests: `@pytest.mark.parametrize('a,b', [(1,2),(3,4)])`.
* Skip/xfail: `@pytest.mark.skip(reason='...')`, `@pytest.mark.xfail`.
* Config file `pytest.ini` for options:
  ```ini
  [pytest]
  addopts = -ra -q
  markers =
      slow: mark test as slow
  ```
* Run with coverage: `pytest --cov=module --cov-report=html`.
* Debug failing tests: `pytest --pdb` or insert `import pdb; pdb.set_trace()`.
* Use `capsys` fixture to capture stdout/stderr.
* Plugins extend behavior (e.g. `pytest-mock`, `pytest-cov`, `pytest-asyncio`).

These notes kept shorter later results simply because earlier snippets were written more verbosely; subsequent ones were streamlined once the pattern was established. Feel free to expand any section if you want more detail!
