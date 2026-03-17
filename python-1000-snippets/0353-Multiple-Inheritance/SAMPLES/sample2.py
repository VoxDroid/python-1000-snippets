# sample2.py
# Diamond inheritance with super() to ensure each class runs

class Base:
    def action(self):
        return ["Base"]


class Left(Base):
    def action(self):
        return ["Left"] + super().action()


class Right(Base):
    def action(self):
        return ["Right"] + super().action()


class Child(Left, Right):
    def action(self):
        return ["Child"] + super().action()


def main():
    c = Child()
    print("MRO:", [cls.__name__ for cls in Child.__mro__])
    print("action:", c.action())


if __name__ == "__main__":
    main()
