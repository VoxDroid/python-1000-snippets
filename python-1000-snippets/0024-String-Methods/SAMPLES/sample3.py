# sample3.py
# Split a sentence into words and join them in reverse order.

def reverse_words(sentence):
    words = sentence.split()
    return " ".join(reversed(words))

if __name__ == '__main__':
    s = "Python is fun"
    print(reverse_words(s))

