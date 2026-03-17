# 0387-Advanced-Mocking-Techniques Cheatsheet

- Use `unittest.mock.patch` to replace objects during tests.
- `patch` can be used as a decorator or context manager.
- Use `Mock`/`MagicMock` to configure return values and assert calls.
- Patch the object where it is looked up (import location).
