# sample3.py
# Reverse each word in a sentence while preserving word order

if __name__ == '__main__':
    sentence = input("Enter a sentence: ")
    reversed_words = [w[::-1] for w in sentence.split()]
    print(" ".join(reversed_words))
