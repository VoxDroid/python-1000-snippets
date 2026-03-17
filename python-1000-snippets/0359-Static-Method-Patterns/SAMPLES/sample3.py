# sample3.py
# Static methods can be used without creating class instances

class Converter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9 / 5) + 32


def main():
    print("0C ->", Converter.celsius_to_fahrenheit(0), "F")
    print("100C ->", Converter.celsius_to_fahrenheit(100), "F")


if __name__ == "__main__":
    main()
