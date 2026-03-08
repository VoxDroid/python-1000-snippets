# sample2.py
# Play using a fixed sequence of guesses to illustrate both win and lose

import random

words = ['apple']
word = random.choice(words)

def play(guesses):
    guessed = set()
    mistakes = 0
    max_mistakes = 3
    display = ['_' for _ in word]
    for g in guesses:
        if g in guessed:
            continue
        guessed.add(g)
        if g in word:
            for i, l in enumerate(word):
                if l == g:
                    display[i] = g
        else:
            mistakes += 1
        print('Guess', g, '->', ' '.join(display), 'mistakes', mistakes)
    print('Result:', 'win' if '_' not in display else 'lose')

if __name__ == '__main__':
    print('Scenario1')
    play(['a','p','l','e'])
    print('Scenario2')
    play(['x','y','z'])
