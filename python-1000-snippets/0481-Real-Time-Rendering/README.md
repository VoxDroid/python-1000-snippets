# Real-Time Rendering

## Description
This snippet demonstrates a simple rendering loop using `pygame`.

## Code
```python
# Note: Requires `pygame`. Install with `pip install pygame`
try:
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    screen.fill((255, 0, 0))
    pygame.display.flip()
    print("Screen rendered")
    pygame.quit()
except ImportError:
    print("Mock Output: Screen rendered")
```

## Output
```
Mock Output: Screen rendered
```
*(Real output with `pygame`: `Screen rendered` (displays red screen))*

## Explanation
- **Real-Time Rendering**: Renders a red screen using Pygame.
- **Logic**: Fills the screen with a color and updates the display.
- **Complexity**: O(1) per frame.
- **Use Case**: Used in games or interactive graphics.
- **Best Practice**: Optimize draw calls; handle events; manage frame rate.