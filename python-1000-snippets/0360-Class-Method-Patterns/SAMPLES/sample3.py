# sample3.py
# Class methods working correctly with subclasses

class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    @classmethod
    def with_wheels(cls, count):
        return cls(count)


class Car(Vehicle):
    pass


def main():
    c = Car.with_wheels(4)
    print("Car wheels:", c.wheels)


if __name__ == "__main__":
    main()
