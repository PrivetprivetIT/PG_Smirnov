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

width = 100
height = 75

rects = []

rects.append(pygame.Rect(0, 0, width, height))

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].topright = (size[0], 0)

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomleft = (0, size[1])

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].bottomright = (size[0], size[1])

rects.append(pygame.Rect(0, 0, width, height))
rects[-1].center = (size[0] // 2, size[1] // 2)

FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for rect in rects:
        color = random.choice(colors)
        pygame.draw.rect(screen, color, rect)


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()