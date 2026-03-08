# sample2.py
# Replayable game: ask user if they want to play again

import random

def play():
    secret = random.randint(1, 50)
    while True:
        guess = int(input('Guess: '))
        if guess == secret:
            print('Win')
            break
        elif guess < secret:
            print('Low')
        else:
            print('High')

if __name__ == '__main__':
    while True:
        play()
        ans = input('Play again? (y/n) ')
        if ans.lower() != 'y':
            break
