# Rock Paper Scissors Cheatsheet

## Rules
- rock beats scissors
- scissors beats paper
- paper beats rock

## Random choice
```python
import random
computer = random.choice(['rock','paper','scissors'])
```

## Helper
```
def winner(u,c):
    if u==c: return 'tie'
    # use a dict mapping
```

## Tips
- Validate user input to one of allowed values.
- You can implement best-of-N easily with loops.

## Running samples
Activate venv and pipe inputs to `SAMPLES/sample*.py`.
