# sample3.py
# Demonstrate default and keyword arguments.

def repeat(message, times=2):
    for _ in range(times):
        print(message)

if __name__ == '__main__':
    repeat("Hello")
    repeat("Hi", times=3)

