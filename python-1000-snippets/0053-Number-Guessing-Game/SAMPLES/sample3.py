# sample3.py
# Limited attempts and input validation

import random

if __name__ == '__main__':
    secret = random.randint(1, 20)
    attempts = 0
    max_attempts = 5
    while attempts < max_attempts:
        try:
            guess = int(input('Guess: '))
        except ValueError:
            print('Not a number')
            continue
        attempts += 1
        if guess == secret:
            print('Correct')
            break
        print('Too low' if guess < secret else 'Too high')
    else:
        print('Out of attempts, secret was', secret)
