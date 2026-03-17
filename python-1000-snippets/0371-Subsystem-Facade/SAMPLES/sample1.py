# sample1.py
# Basic facade that combines two subsystems

class SubsystemA:
    def operation_a(self):
        return "Subsystem A"


class SubsystemB:
    def operation_b(self):
        return "Subsystem B"


class Facade:
    def __init__(self):
        self.sub_a = SubsystemA()
        self.sub_b = SubsystemB()

    def operation(self):
        return f"{self.sub_a.operation_a()} + {self.sub_b.operation_b()}"


def main():
    facade = Facade()
    print(facade.operation())


if __name__ == "__main__":
    main()
