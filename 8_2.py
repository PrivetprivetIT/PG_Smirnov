from all_colors import *

import pygame
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя игра')
BACKGROUND = BLACK
screen.fill(BACKGROUND)

LINE_COLOR = (255, 255, 255)
PREVIEW_COLOR = (192, 192, 192)

points = []

FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            points.append(event.pos)



    screen.fill(BACKGROUND)

    for i in range(len(points) - 1):
        start_point = points[i]
        end_point = points[i+1]
        pygame.draw.line(screen, LINE_COLOR, start_point, end_point, 3)
    if len(points) > 1:
        mouse_pos = pygame.mouse.get_pos()
        last_point = points[i+1]
        pygame.draw.aaline(screen, PREVIEW_COLOR, last_point, mouse_pos, 2)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
