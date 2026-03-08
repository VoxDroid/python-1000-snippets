# sample2.py
# post a QUIT event to exit immediately

import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
import pygame

pygame.init()
screen = pygame.display.set_mode((100,100))
pygame.event.post(pygame.event.Event(pygame.QUIT))

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()
print('quit event processed')
