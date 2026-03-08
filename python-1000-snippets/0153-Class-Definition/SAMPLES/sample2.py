# sample2.py
# class with class variable and __str__

class Counter:
    instances = 0
    def __init__(self):
        Counter.instances += 1
    def __str__(self):
        return f"Counter({Counter.instances})"

if __name__ == '__main__':
    c1 = Counter()
    c2 = Counter()
    print(c1)
    print(c2)
    print('total instances', Counter.instances)    
