# sample3.py
# Loop until a valid integer between 1 and 10 is entered.

def prompt_number():
    while True:
        try:
            n = int(input("Enter a number 1-10: ").strip())
            if 1 <= n <= 10:
                return n
            print("Number out of range")
        except ValueError:
            print("That's not an integer")

if __name__ == '__main__':
    choice = prompt_number()
    print(f"You selected {choice}")

