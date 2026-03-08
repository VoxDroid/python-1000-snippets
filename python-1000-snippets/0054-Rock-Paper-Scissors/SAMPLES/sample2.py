# sample2.py
# Best-of-three match keeping score

import random

def play_round():
    choices = ['rock', 'paper', 'scissors']
    user = input('Your choice: ').strip().lower()
    comp = random.choice(choices)
    print('Computer:', comp)
    if user == comp:
        return 0
    if (user == 'rock' and comp == 'scissors') or \
       (user == 'paper' and comp == 'rock') or \
       (user == 'scissors' and comp == 'paper'):
        return 1
    return -1

if __name__ == '__main__':
    score = 0
    for i in range(3):
        res = play_round()
        score += res
    if score > 0:
        print('You win match')
    elif score < 0:
        print('Computer wins match')
    else:
        print('Match tie')
