# sample3.py
# Use a helper function and mapping dictionary to decide winner

import random

rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

def winner(user, comp):
    if user == comp:
        return 'tie'
    if rules.get(user) == comp:
        return 'user'
    return 'computer'

if __name__ == '__main__':
    choices = list(rules.keys())
    user = input('> ').strip().lower()
    comp = random.choice(choices)
    print('comp:', comp)
    result = winner(user, comp)
    print('result:', result)
