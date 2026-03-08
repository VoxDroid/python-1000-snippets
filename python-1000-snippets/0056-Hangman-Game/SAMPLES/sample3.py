# sample3.py
# Interactive hangman reading guesses from stdin

import random
import sys

words = ['banana', 'cherry', 'date']
word = random.choice(words)

guessed = set()
mistakes = 0
max_mistakes = 5
display = ['_' for _ in word]

for line in sys.stdin:
    guess = line.strip().lower()
    if not guess:
        continue
    if guess in guessed:
        print('Already guessed', guess)
        continue
    guessed.add(guess)
    if guess in word:
        for i, l in enumerate(word):
            if l == guess:
                display[i] = guess
    else:
        mistakes += 1
        print('Wrong! attempts left', max_mistakes - mistakes)
    print('Word:', ' '.join(display))
    if mistakes >= max_mistakes or '_' not in display:
        break
print('Final word:', word)
print('Win' if '_' not in display else 'Lose')
