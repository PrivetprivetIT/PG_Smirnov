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
lines = []

FPS = 60
clock = pygame.time.Clock()

show_preview = True

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                points.append(event.pos)
            elif event.button == 3:
                if len(points) > 0:
                    lines.append(points.copy())
                    points.clear()


    screen.fill(BACKGROUND)

    for line in lines:
        if len(line) > 1:
            pygame.draw.lines(screen, LINE_COLOR, False, line, 3)

    if len(points) > 1:
        pygame.draw.lines(screen, LINE_COLOR, False, points, 3)

    if len(points) > 0 and show_preview:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.aaline(screen, PREVIEW_COLOR, points[-1], mouse_pos, 2)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
