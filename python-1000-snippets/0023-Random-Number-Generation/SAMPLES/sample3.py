# sample3.py
# Shuffle a deck of cards represented as strings.

import random

def main():
    deck = [f"{rank}{suit}" for rank in "A23456789TJQK" for suit in "♠♥♦♣"]
    random.shuffle(deck)
    print(deck[:5], "... shuffled deck ...")

if __name__ == '__main__':
    main()

