# sample1.py
# Ask the user for numbers and append them to a list until they enter blank.

def main():
    nums = []
    while True:
        s = input("Enter a number (blank to finish): ")
        if not s:
            break
        try:
            n = float(s)
        except ValueError:
            print("Invalid")
            continue
        nums.append(n)
    print("You entered:", nums)

if __name__ == '__main__':
    main()

