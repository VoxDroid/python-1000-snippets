# sample2.py
# Test multiple strings for palindrome status.

def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

strings = ["Racecar", "hello", "A man, a plan, a canal: Panama"]
for s in strings:
    print(s, "->", is_palindrome(s))

