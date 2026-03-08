# sample2.py
# Filter out empty strings from a list

if __name__ == '__main__':
    strings = ["hello", "", "world", " ", "python"]
    nonempty = list(filter(None, strings))
    print('strings:', strings)
    print('non-empty:', nonempty)
