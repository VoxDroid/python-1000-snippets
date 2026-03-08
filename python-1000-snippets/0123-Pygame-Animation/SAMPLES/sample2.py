# sample2.py
# multiple objects animation

import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
import pygame

FPS = 30
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 150

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
positions = [0, 50, 100]
for _ in range(3):
    screen.fill((0,0,0))
    for i,p in enumerate(positions):
        pygame.draw.circle(screen, (255,255,0), (p, 50 + i*30), 10)
        positions[i] = (p + 15) % WINDOW_WIDTH
    pygame.display.flip()
pygame.quit()
print('multiple circles moved')
