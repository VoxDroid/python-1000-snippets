# sample3.py
# factory method in base class overridden by subclasses

class Logger:
    def log(self, msg):
        raise NotImplementedError
    @classmethod
    def create(cls):
        return cls()

class FileLogger(Logger):
    def log(self, msg):
        return f'file:{msg}'

class ConsoleLogger(Logger):
    def log(self, msg):
        return f'console:{msg}'

if __name__ == '__main__':
    print(FileLogger.create().log('hi'))
    print(ConsoleLogger.create().log('hi'))
