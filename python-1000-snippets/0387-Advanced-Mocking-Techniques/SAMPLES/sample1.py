# sample1.py
# Mocking a function using unittest.mock.patch

from unittest.mock import patch


def get_data():
    return "Real data"


def main():
    with patch("__main__.get_data", return_value="Mocked data"):
        print(get_data())


if __name__ == "__main__":
    main()
