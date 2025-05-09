# Hangman Game

## Description
This snippet implements a Hangman game where the user guesses letters to reveal a randomly chosen word, with a limited number of incorrect guesses.

## Code
```python
import random

words = ["python", "coding", "game"]
word = random.choice(words)
guessed = set()
mistakes = 0
max_mistakes = 6
display = ["_" for _ in word]

while mistakes < max_mistakes and "_" in display:
    print("Word:", " ".join(display))
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print("Already guessed!")
        continue
    guessed.add(guess)
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                display[i] = guess
    else:
        mistakes += 1
        print(f"Wrong! {max_mistakes - mistakes} attempts left.")
print("Word:", "".join(display))
print("You win!" if "_" not in display else f"You lose! Word was {word}.")
```

## Output
```
Word: _ _ _ _ _ _
Guess a letter: p
Word: p _ _ _ _ _
Guess a letter: y
Word: p y _ _ _ _
Guess a letter: x
Wrong! 5 attempts left.
...
Word: python
You win!
```
*(Output varies based on guesses)*

## Explanation
- **Game Logic**: Tracks guessed letters, updates the word display, and counts mistakes.
- **Random Word**: `random.choice(words)` selects a word from a predefined list.
- **Use Case**: Demonstrates loops, conditionals, and string manipulation in an interactive game.
- **Error Handling**: Should validate single-letter inputs in production.
- **Best Practice**: Add a larger word list and input validation for a robust game.