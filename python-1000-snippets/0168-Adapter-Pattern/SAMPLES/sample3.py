# sample3.py
# class adapter via inheritance

class Target:
    def request(self):
        return "Target request"

class Adaptee:
    def specific_request(self):
        return "Adaptee specific"

class ClassAdapter(Target, Adaptee):
    def request(self):
        return self.specific_request()

if __name__ == '__main__':
    adapter = ClassAdapter()
    print(adapter.request())
