# sample3.py
# More efficient trial division skipping even numbers.

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == '__main__':
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Not an integer")
    else:
        print(is_prime(num))

