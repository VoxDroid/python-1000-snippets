# sample3.py
# draw random rectangles

import os, random
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
import pygame

pygame.init()
screen = pygame.display.set_mode((200, 150))
for _ in range(5):
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    rect = (random.randint(0,150), random.randint(0,100), 30, 30)
    pygame.draw.rect(screen, color, rect)
pngfile = 'out.png'
pygame.image.save(screen, pngfile)
pygame.quit()
print('saved', pngfile)
