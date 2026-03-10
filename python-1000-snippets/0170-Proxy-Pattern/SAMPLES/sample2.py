# sample2.py
# virtual proxy delaying expensive initialization

class Heavy:
    def __init__(self):
        print('Heavy init')
        self.data = [0] * 1000000
    def operate(self):
        return 'operated'

class VirtualProxy:
    def __init__(self):
        self._real = None
    def operate(self):
        if self._real is None:
            self._real = Heavy()
        return self._real.operate()

if __name__ == '__main__':
    proxy = VirtualProxy()
    print('before call')
    print(proxy.operate())
    print('after call')
