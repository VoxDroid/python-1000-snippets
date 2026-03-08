# sample3.py
# Check if a number is a palindrome by converting to string.

def is_palindrome_number(n):
    s = str(n)
    return s == s[::-1]

if __name__ == '__main__':
    for num in [121, 123, 44, 10]:
        print(num, is_palindrome_number(num))

