# sample3.py
# bouncing square example

import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
import pygame

WINDOW_WIDTH = 200
WINDOW_HEIGHT = 150

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
x, y = 0, 0
dx, dy = 5, 3
for _ in range(20):
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0,128,0), (x, y, 20, 20))
    pygame.display.flip()
    x += dx
    y += dy
    if x < 0 or x > WINDOW_WIDTH-20: dx = -dx
    if y < 0 or y > WINDOW_HEIGHT-20: dy = -dy
pygame.quit()
print('bouncing square done')
