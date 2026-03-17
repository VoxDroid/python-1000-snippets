# sample2.py
# Adapter for a third-party API

class ThirdPartyLogger:
    def log(self, message):
        return f"LOG: {message}"


class LoggerInterface:
    def write(self, message):
        raise NotImplementedError


class LoggerAdapter(LoggerInterface):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def write(self, message):
        return self.adaptee.log(message)


def main():
    third_party = ThirdPartyLogger()
    logger = LoggerAdapter(third_party)
    print(logger.write("Hello"))


if __name__ == "__main__":
    main()
