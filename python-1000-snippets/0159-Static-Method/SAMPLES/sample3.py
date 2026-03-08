# sample3.py
# staticmethod vs classmethod demonstration

class Demo:
    @staticmethod
    def static():
        return 'static called'
    @classmethod
    def klass(cls):
        return f'class called on {cls.__name__}'

if __name__ == '__main__':
    print(Demo.static())
    print(Demo.klass())
    d = Demo()
    print(d.static(), d.klass())
