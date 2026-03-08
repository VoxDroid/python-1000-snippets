# sample1.py
# simulate a click and observe background change

import os, random
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
import pygame

pygame.init()
screen = pygame.display.set_mode((100,100))
pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))

bg = (255,255,255)
for _ in range(3):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            bg = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    screen.fill(bg)
    pygame.display.flip()
pygame.quit()
print('click handled')
