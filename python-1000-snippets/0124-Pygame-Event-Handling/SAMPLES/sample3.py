# sample3.py
# cycle background through random colors on each synthesized click

import os, random
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
import pygame

pygame.init()
screen = pygame.display.set_mode((100,100))

bg = (255,255,255)
for i in range(5):
    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            bg = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    screen.fill(bg)
    pygame.display.flip()
pygame.quit()
print('cycle done')
