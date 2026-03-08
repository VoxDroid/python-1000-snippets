# sample1.py
# Hangman with seeded word.choice so outcome is deterministic

import random

words = ['python', 'coding', 'game']
random.seed(0)
word = random.choice(words)

guessed = set()
mistakes = 0
max_mistakes = 6
display = ['_' for _ in word]

for guess in ['p', 'y', 't', 'h', 'o', 'n']:
    if guess in guessed:
        continue
    guessed.add(guess)
    if guess in word:
        for i, l in enumerate(word):
            if l == guess:
                display[i] = guess
    else:
        mistakes += 1
    print('Word:', ' '.join(display))
print('Final:', ''.join(display))
print('Win' if '_' not in display else 'Lose')
