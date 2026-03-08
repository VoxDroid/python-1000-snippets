# sample2.py
# validate numeric input and compute square

def main():
    while True:
        val = input("Enter a number: ")
        try:
            num = float(val)
            break
        except ValueError:
            print("Not a number, try again.")
    print(f"Square: {num * num}")

if __name__ == '__main__':
    main()

