# sample2.py
# singleton implemented via metaclass

class SingletonMeta(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Logger(metaclass=SingletonMeta):
    pass

if __name__ == '__main__':
    print('same?', Logger() is Logger())
