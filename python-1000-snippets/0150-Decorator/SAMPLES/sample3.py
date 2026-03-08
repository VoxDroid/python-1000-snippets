# sample3.py
# decorator with arguments (repeat n times)

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def hello():
    print('hello')

if __name__ == '__main__':
    hello()
