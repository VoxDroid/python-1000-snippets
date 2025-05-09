# Number Guessing Game

## Description
This snippet implements a number guessing game where the user tries to guess a random number between 1 and 100, with hints provided.

## Code
```python
import random

secret = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1
    if guess == secret:
        print(f"Correct! It took {attempts} attempts.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
```

## Output
```
Guess a number (1-100): 50
Too low!
Guess a number (1-100): 75
Too high!
Guess a number (1-100): 62
Correct! It took 3 attempts.
```
*(Output varies based on guesses)*

## Explanation
- **Game Logic**: Generates a random number (`secret`) and compares user guesses, providing "too high" or "too low" hints.
- **Loop**: Continues until the correct number is guessed, tracking attempts.
- **Use Case**: Demonstrates user interaction, conditionals, and loops in a fun application.
- **Error Handling**: Should catch non-integer inputs in production.
- **Best Practice**: Add a maximum attempt limit or input validation for robustness.