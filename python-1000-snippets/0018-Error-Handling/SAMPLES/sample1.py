# sample1.py
# Show catching ValueError and ZeroDivisionError

def main():
    try:
        x = int(input("Enter integer: "))
        print(10 / x)
    except ValueError:
        print("Not a valid integer")
    except ZeroDivisionError:
        print("Cannot divide by zero")

if __name__ == '__main__':
    main()

