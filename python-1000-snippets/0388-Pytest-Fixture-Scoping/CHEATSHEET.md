# 0388-Pytest-Fixture-Scoping Cheatsheet

- `scope="function"`: fixture is created for each test function (default).
- `scope="module"`: fixture shared across tests in a module.
- `scope="session"`: fixture shared across the entire test session.
- Use `yield` fixtures to provide teardown logic.
