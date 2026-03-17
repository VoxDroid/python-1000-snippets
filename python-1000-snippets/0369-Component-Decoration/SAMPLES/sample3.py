# sample3.py
# Decorator adding logging behavior to a component

class Component:
    def operation(self):
        return "Doing work"


class LoggingDecorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        print("[LOG] before")
        result = self.component.operation()
        print("[LOG] after")
        return result


def main():
    base = Component()
    logged = LoggingDecorator(base)
    print(logged.operation())


if __name__ == "__main__":
    main()
