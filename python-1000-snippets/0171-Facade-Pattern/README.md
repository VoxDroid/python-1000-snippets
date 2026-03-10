# 0171-Facade-Pattern

## Description
This snippet demonstrates the Facade pattern by providing a simple interface to a set of complex subsystems. A `ComputerFacade` class hides the details of starting various components like CPU, memory and disk.

## Code
```python
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

computer = ComputerFacade()
computer.start()
```

## Output
```
CPU freeze
Disk read 1024 bytes from 0
Memory load from 0 data: data
CPU jump to 0
CPU execute
```

## Explanation
- **Facade**: `ComputerFacade` provides a high-level `start` method while hiding the complex interactions between CPU, Memory and Disk.
- **Logic**: Client interacts only with façade; subsystems are instantiated internally.
- **Complexity**: O(1) façade operation regardless of underlying steps.
- **Use Case**: Simplify API surface, decouple client from subsystems, reduce dependencies.
- **Variation**: Multiple facades for different scenarios (e.g. home theater system).
