# sample1.py
# Basic guessing game with seeded random for deterministic secret

import random

if __name__ == '__main__':
    random.seed(0)
    secret = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input())
        attempts += 1
        if guess == secret:
            print('Correct after', attempts, 'attempts')
            break
        elif guess < secret:
            print('Too low')
        else:
            print('Too high')
