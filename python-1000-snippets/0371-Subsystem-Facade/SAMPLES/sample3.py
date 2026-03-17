# sample3.py
# Facade hiding configuration of multiple subsystems

class SubsystemA:
    def __init__(self, value):
        self.value = value

    def operation_a(self):
        return f"A({self.value})"


class SubsystemB:
    def __init__(self, value):
        self.value = value

    def operation_b(self):
        return f"B({self.value})"


class Facade:
    def __init__(self, config):
        self.sub_a = SubsystemA(config.get("a", 1))
        self.sub_b = SubsystemB(config.get("b", 2))

    def perform(self):
        return f"{self.sub_a.operation_a()} + {self.sub_b.operation_b()}"


def main():
    facade = Facade({"a": 10, "b": 20})
    print(facade.perform())


if __name__ == "__main__":
    main()
