# Facade Pattern

## Description
This snippet implements the Facade pattern to provide a simplified interface to a complex subsystem.

## Code
```python
class CPU:
    def process(self):
        return "CPU processing"

class Memory:
    def load(self):
        return "Memory loading"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
    def start(self):
        return f"{self.memory.load()} -> {self.cpu.process()}"

computer = ComputerFacade()
print(computer.start())
```

## Output
```
Memory loading -> CPU processing
```

## Explanation
- **Facade Pattern**: `ComputerFacade` simplifies interaction with `CPU` and `Memory` subsystems.
- **Logic**: `start` orchestrates subsystem calls into a single method.
- **Complexity**: O(1) for facade operations.
- **Use Case**: Used to simplify complex APIs or subsystem interactions.
- **Best Practice**: Keep facade methods focused; avoid exposing subsystem details.