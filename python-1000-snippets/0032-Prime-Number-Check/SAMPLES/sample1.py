# sample1.py
# Prompt user and check prime status.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Not an integer")
    else:
        print(f"{num} is {'prime' if is_prime(num) else 'not prime'}.")

