# sample1.py
# initialize a pygame window and immediately exit

import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
import pygame

FPS = 60
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 150

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Test Window')

# draw one frame and quit
screen.fill((0, 128, 0))
pygame.display.flip()
pygame.quit()
print('initialized and closed window')
