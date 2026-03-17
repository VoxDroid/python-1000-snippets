# sample2.py
# Mocking a class to control behavior in a test

from unittest.mock import MagicMock, patch


class Service:
    def fetch(self):
        return "real"


def process(service: Service):
    return service.fetch().upper()


def main():
    mock_service = MagicMock(spec=Service)
    mock_service.fetch.return_value = "mocked"
    print(process(mock_service))

    # Using patch to mock the Service class
    with patch("__main__.Service") as MockService:
        MockService.return_value.fetch.return_value = "patched"
        print(process(Service()))


if __name__ == "__main__":
    main()
