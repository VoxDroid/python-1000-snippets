# sample1.py
# draw a red rectangle and a blue circle once

import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
import pygame

pygame.init()
screen = pygame.display.set_mode((200, 150))
pygame.draw.rect(screen, (255, 0, 0), (20, 20, 100, 50))
pygame.draw.circle(screen, (0, 0, 255), (150, 75), 30)
pygame.display.flip()
pygame.quit()
print('drew shapes')
