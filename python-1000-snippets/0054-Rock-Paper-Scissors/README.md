# Rock Paper Scissors

## Description
This snippet implements a Rock Paper Scissors game where the user competes against the computer, with random choices.

## Code
```python
import random

choices = ["rock", "paper", "scissors"]
user = input("Enter rock, paper, or scissors: ").lower()
computer = random.choice(choices)
print(f"Computer chose: {computer}")
if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("Computer wins!")
```

## Output
```
Enter rock, paper, or scissors: rock
Computer chose: scissors
You win!
```
*(Output varies based on choices)*

## Explanation
- **Game Logic**: Compares user and computer choices to determine the winner based on rules (rock > scissors, paper > rock, scissors > paper).
- **Random Choice**: `random.choice()` selects the computer’s move.
- **Use Case**: Demonstrates conditionals, user input, and randomization in a simple game.
- **Error Handling**: Should validate user input (e.g., only allow valid choices).
- **Best Practice**: Add a loop for multiple rounds and track scores for a full game.