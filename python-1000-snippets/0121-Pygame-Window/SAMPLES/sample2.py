# sample2.py
# change background color over a few frames

import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
import pygame

FPS = 30
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 150

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Color Cycle')

colors = [(255,0,0),(0,255,0),(0,0,255)]
for c in colors:
    screen.fill(c)
    pygame.display.flip()
pygame.quit()
print('color cycle done')
