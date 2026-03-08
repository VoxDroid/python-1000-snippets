# sample2.py
# Read values from user input and use variables in a calculation.

def main():
    try:
        base = float(input("Enter base length: "))
        height = float(input("Enter height: "))
    except ValueError:
        print("Please enter numeric values.")
        return
    area = 0.5 * base * height
    print(f"Triangle area is {area}")

if __name__ == '__main__':
    main()

