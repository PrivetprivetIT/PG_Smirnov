from all_colors import *

import pygame
pygame.init()


def remove_point(mouse_pos):
    for point in points:
        if ((point[0] - mouse_pos[0])**2 + (point[1] - mouse_pos[1])**2
                <= POINT_RADIUS **2):
            points.remove(point)
            break

def highlight_closest_point(mouse_pos):
    clossest_point = None
    clossest_distance = float('inf')
    for point in points:
        distance = ((point[0] - mouse_pos[0])**2 + (point[1] - mouse_pos[1])**2)**0.5
        if distance <= POINT_RADIUS**2 and distance < clossest_distance:
            clossest_point = point
            clossest_distance = distance
    if clossest_point is not None:
        pygame.draw.circle(screen, HIGHLIGHT_COlOR, clossest_point, POINT_RADIUS)

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя игра')
BACKGROUND = BLACK
screen.fill(BACKGROUND)

LINE_COLOR = (255, 255, 255)
PREVIEW_COLOR = (192, 192, 192)
HIGHLIGHT_COlOR = (255, 0, 0)
POINT_RADIUS = 5
points = []

FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                points.append(event.pos)

            if event.button == 3:
                remove_point(event.pos)

    screen.fill(BACKGROUND)

    for i in range(len(points) - 1):
        start_point = points[i]
        end_point = points[i+1]
        pygame.draw.line(screen, LINE_COLOR, start_point, end_point, 3)
    if len(points) > 0:
        mouse_pos = pygame.mouse.get_pos()
        last_point = points[-1]
        pygame.draw.aaline(screen, PREVIEW_COLOR, last_point, mouse_pos, 2)


    highlight_closest_point(pygame.mouse.get_pos())

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
