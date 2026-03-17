# sample2.py
# Duck typing: accept any object with a required method

class Bird:
    def fly(self):
        return "bird flying"


class Airplane:
    def fly(self):
        return "airplane soaring"


def take_off(flyer):
    print(flyer.fly())


def main():
    take_off(Bird())
    take_off(Airplane())


if __name__ == "__main__":
    main()
