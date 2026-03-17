# sample2.py
# Facade that handles errors from subsystems

class SubsystemA:
    def operation_a(self):
        return "A"


class SubsystemB:
    def operation_b(self):
        raise RuntimeError("B failed")


class Facade:
    def __init__(self):
        self.sub_a = SubsystemA()
        self.sub_b = SubsystemB()

    def operation(self):
        try:
            return f"{self.sub_a.operation_a()} + {self.sub_b.operation_b()}"
        except Exception as e:
            return f"error: {e}"


def main():
    facade = Facade()
    print(facade.operation())


if __name__ == "__main__":
    main()
