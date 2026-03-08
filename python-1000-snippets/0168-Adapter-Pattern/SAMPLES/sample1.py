# sample1.py
# basic adapter example from README

class OldSystem:
    def old_request(self):
        return "Old system response"

class NewSystem:
    def new_request(self):
        pass

class Adapter(NewSystem):
    def __init__(self, old_system):
        self.old_system = old_system
    def new_request(self):
        return self.old_system.old_request()

if __name__ == '__main__':
    old = OldSystem()
    adapter = Adapter(old)
    print(adapter.new_request())
