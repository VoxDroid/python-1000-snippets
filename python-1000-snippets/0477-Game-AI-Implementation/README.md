# Game AI Implementation

## Description
This snippet demonstrates a simple game AI using `pygame`.

## Code
```python
# Note: Requires `pygame`. Install with `pip install pygame`
try:
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    player = pygame.Rect(50, 50, 10, 10)
    if player.x < 75:
        player.x += 5
    print("AI moved player")
    pygame.quit()
except ImportError:
    print("Mock Output: AI moved player")
```

## Output
```
Mock Output: AI moved player
```
*(Real output with `pygame`: `AI moved player`)*

## Explanation
- **Game AI Implementation**: Moves a player based on a simple rule.
- **Logic**: Updates player position if condition is met.
- **Complexity**: O(1) per update.
- **Use Case**: Used in game development for NPC behavior.
- **Best Practice**: Implement state machines; handle collisions; test AI logic.