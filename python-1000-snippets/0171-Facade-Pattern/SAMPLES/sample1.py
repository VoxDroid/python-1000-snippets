# sample1.py
# computer startup facade (from README)

class CPU:
    def freeze(self):
        print("CPU freeze")
    def jump(self, position):
        print(f"CPU jump to {position}")
    def execute(self):
        print("CPU execute")

class Memory:
    def load(self, position, data):
        print(f"Memory load from {position} data: {data}")

class Disk:
    def read(self, lba, size):
        print(f"Disk read {size} bytes from {lba}")
        return "data"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.disk = Disk()
    def start(self):
        self.cpu.freeze()
        self.disk.read(0, 1024)
        self.memory.load(0, "data")
        self.cpu.jump(0)
        self.cpu.execute()

if __name__ == '__main__':
    comp = ComputerFacade()
    comp.start()
