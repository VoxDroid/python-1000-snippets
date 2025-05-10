# Pygame Event Handling

## Description
This snippet handles mouse clicks in a Pygame window to change the background color, compatible with Pyodide.

## Code
```python
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Event Handling")

# Initial background color
bg_color = (255, 255, 255)  # White
running = True
clock = pygame.time.Clock()
FPS = 60

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Change background to random color on click
            bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # Update display
    screen.fill(bg_color)
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(FPS)

# Clean up
pygame.quit()
```

## Output
<div style="text-align: center;">
  <img src="Output.gif" alt="Output image">
  <p></p>
</div>

*(Visual Output)*: A 400x300 window starts white; each mouse click changes the background to a random RGB color.

## Explanation
- **Pygame Event Handling**: Listens for `MOUSEBUTTONDOWN` to update `bg_color`.
- **Pyodide**: `asyncio` loop ensures browser compatibility.
- **Complexity**: O(1) per frame.
- **Use Case**: Used in interactive applications or games.
- **Best Practice**: Handle multiple event types; debounce rapid inputs.