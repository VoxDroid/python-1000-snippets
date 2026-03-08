# sample3.py
# Simple game: roll two dice, highest total wins

import random

def roll_dice(sides, rolls):
    return sum(random.randint(1, sides) for _ in range(rolls))

if __name__ == '__main__':
    sides = int(input('sides: '))
    rolls = int(input('rolls: '))
    player1 = roll_dice(sides, rolls)
    player2 = roll_dice(sides, rolls)
    print('p1 total', player1, 'p2 total', player2)
    if player1 > player2:
        print('Player 1 wins')
    elif player2 > player1:
        print('Player 2 wins')
    else:
        print('Tie')
