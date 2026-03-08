# sample3.py
# draw a moving square for a few steps

import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
import pygame

WINDOW_WIDTH = 200
WINDOW_HEIGHT = 150

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Moving Square')

x = 0
for _ in range(5):
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0,0,255), (x, 50, 20, 20))
    pygame.display.flip()
    x += 10
pygame.quit()
print('animation done')
