# sample3.py
# Sum numbers entered by the user until they enter 0.

def main():
    total = 0
    while True:
        try:
            n = float(input("Enter number (0 to stop): "))
        except ValueError:
            print("Invalid input")
            continue
        if n == 0:
            break
        total += n
    print("Total sum:", total)

if __name__ == '__main__':
    main()

