# sample1.py
# simple circle moving automatically

import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
import pygame

FPS = 30
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 150

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
x = 0
for _ in range(5):
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,0,255), (x, 75), 20)
    pygame.display.flip()
    x = (x + 20) % WINDOW_WIDTH
pygame.quit()
print('circle moved')
