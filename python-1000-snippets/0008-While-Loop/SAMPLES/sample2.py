# sample2.py
# Prompt user for a secret word until they guess correctly.

SECRET = "python"

def main():
    guess = ""
    while guess != SECRET:
        guess = input("Guess the secret word: ")
    print("Correct!")

if __name__ == '__main__':
    main()

