# sample1.py
# simple protection proxy example (from README)

class Resource:
    def access(self):
        return "Accessing resource"

class Proxy:
    def __init__(self):
        self._resource = Resource()
    def access(self):
        print("Proxy checking access...")
        return self._resource.access()

if __name__ == '__main__':
    proxy = Proxy()
    print(proxy.access())
