# sample3.py
# logging proxy using __getattr__ for delegation

class Subject:
    def method(self, x):
        return x * 2

class LoggingProxy:
    def __init__(self, subject):
        self._subject = subject
    def __getattr__(self, name):
        attr = getattr(self._subject, name)
        if callable(attr):
            def wrapper(*args, **kwargs):
                print(f"calling {name} with", args, kwargs)
                return attr(*args, **kwargs)
            return wrapper
        return attr

if __name__ == '__main__':
    subj = Subject()
    proxy = LoggingProxy(subj)
    print(proxy.method(5))
