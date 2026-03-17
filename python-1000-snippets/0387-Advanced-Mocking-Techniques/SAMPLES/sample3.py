# sample3.py
# Mocking a context manager using patch

from unittest.mock import patch, MagicMock


class Resource:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        pass

    def read(self):
        return "data"


def main():
    with patch("__main__.Resource") as MockResource:
        instance = MockResource.return_value
        instance.read.return_value = "mocked"
        with Resource() as r:
            print(r.read())


if __name__ == "__main__":
    main()
