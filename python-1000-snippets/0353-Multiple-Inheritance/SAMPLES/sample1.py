# sample1.py
# Simple multiple inheritance with explicit method resolution

class A:
    def feature(self):
        return "Feature A"


class B:
    def feature(self):
        return "Feature B"


class C(A, B):
    pass


def main():
    obj = C()
    print("C MRO:", [cls.__name__ for cls in C.__mro__])
    print("feature():", obj.feature())


if __name__ == "__main__":
    main()
