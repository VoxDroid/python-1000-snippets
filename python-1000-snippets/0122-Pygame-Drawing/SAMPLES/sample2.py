# sample2.py
# draw multiple shapes in a loop

import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
import pygame

pygame.init()
screen = pygame.display.set_mode((200, 150))
for i in range(3):
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (255,0,0), (10+i*20, 10, 50, 50))
    pygame.draw.circle(screen, (0,0,255), (100, 75), 20+i*10)
    pygame.display.flip()
pygame.quit()
print('looped shapes')
