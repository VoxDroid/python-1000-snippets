# sample3.py
# Iterate through characters in a string and count vowels.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

if __name__ == '__main__':
    sentence = "The quick brown fox"
    print("Vowel count:", count_vowels(sentence))

