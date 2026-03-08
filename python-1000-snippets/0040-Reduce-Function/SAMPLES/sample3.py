# sample3.py
# Concatenate a list of strings using reduce

from functools import reduce

if __name__ == '__main__':
    words = ["Hello", "world", "from", "reduce"]
    sentence = reduce(lambda a, b: a + " " + b, words)
    print('words:', words)
    print('sentence:', sentence)
