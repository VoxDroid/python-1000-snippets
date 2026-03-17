# sample1.py
# Static method for a utility operation

class MathUtils:
    @staticmethod
    def square(n):
        return n * n


def main():
    print("square(5):", MathUtils.square(5))
    # can also call from an instance
    print("square(6):", MathUtils().square(6))


if __name__ == "__main__":
    main()
