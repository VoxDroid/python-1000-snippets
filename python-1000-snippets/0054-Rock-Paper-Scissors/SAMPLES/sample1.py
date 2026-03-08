# sample1.py
# Single round with seeded random choice for reproducibility

import random

if __name__ == '__main__':
    random.seed(1)
    choices = ['rock', 'paper', 'scissors']
    user = input().strip().lower()
    comp = random.choice(choices)
    print('Computer chose:', comp)
    if user == comp:
        print("It's a tie!")
    elif (user == 'rock' and comp == 'scissors') or \
         (user == 'paper' and comp == 'rock') or \
         (user == 'scissors' and comp == 'paper'):
        print('You win!')
    else:
        print('Computer wins!')
