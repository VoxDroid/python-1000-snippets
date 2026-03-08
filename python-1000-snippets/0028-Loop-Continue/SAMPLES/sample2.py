# sample2.py
# Prompt user for positive numbers, skip invalid ones.

if __name__ == '__main__':
    count = 0
    while count < 3:
        val = input("Enter positive number: ")
        try:
            n = float(val)
        except ValueError:
            print("Not a number")
            continue
        if n <= 0:
            print("Not positive")
            continue
        print("Accepted", n)
        count += 1

