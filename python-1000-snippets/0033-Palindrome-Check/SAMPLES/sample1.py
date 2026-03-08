# sample1.py
# Prompt user and check if the string is a palindrome.

def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

if __name__ == '__main__':
    text = input("Enter a string: ")
    print(f"'{text}' is {'a palindrome' if is_palindrome(text) else 'not a palindrome' }.")

