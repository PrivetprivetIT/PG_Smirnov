from pygame.constants import *
import random
from all_colors import *
import pygame
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя игра')
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

x, y = 0, 0
rect_size = 200
colors = [BLACK, RED]

for i in range(2):
    rect = pygame.Rect(x, y, rect_size/(i+1), rect_size/(i+1))
    rect.center = (screen.get_width() // 2, screen.get_height() // 2)
    pygame.draw.rect(screen, colors[i], rect)


FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()