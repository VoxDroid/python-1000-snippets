# sample3.py
# Swap implementations at runtime using the bridge

class LoggerImplementation:
    def log(self, message):
        raise NotImplementedError


class ConsoleLogger(LoggerImplementation):
    def log(self, message):
        return f"Console: {message}"


class FileLogger(LoggerImplementation):
    def log(self, message):
        return f"File: {message}"


class Logger:
    def __init__(self, impl):
        self.impl = impl

    def log(self, message):
        return self.impl.log(message)


def main():
    logger = Logger(ConsoleLogger())
    print(logger.log("hello"))
    logger.impl = FileLogger()
    print(logger.log("hello"))


if __name__ == "__main__":
    main()
