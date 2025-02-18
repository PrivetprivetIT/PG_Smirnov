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

FPS = 6
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(20):
        color = random.choice(colors)
        rect = pygame.Rect(x, y, rect_size-(i*10), rect_size-(i*10))
        rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        pygame.draw.rect(screen, color, rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()