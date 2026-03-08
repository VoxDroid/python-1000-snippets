# sample2.py
# Loop through a list of fixed words and reverse each

if __name__ == '__main__':
    words = ["abc", "12345", "madam"]
    for w in words:
        print(w, "->", w[::-1])
