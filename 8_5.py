from all_colors import *

import pygame
pygame.init()

def get_clossest_point(mouse_pos):
    clossest_point = None
    clossest_distance = float('inf')
    for point in points:
        distance = ((point[0] - mouse_pos[0])**2 + (point[1] - mouse_pos[1])**2)**0.5
        if distance <= POINT_RADIUS**2 and distance < clossest_distance:
            clossest_point = point
            clossest_distance = distance
    return clossest_point

def remove_point(mouse_pos):
    for point in points:
        if ((point[0] - mouse_pos[0])**2 + (point[1] - mouse_pos[1])**2
                <= POINT_RADIUS **2):
            points.remove(point)
            break


size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя игра')
BACKGROUND = BLACK
screen.fill(BACKGROUND)

LINE_COLOR = (255, 255, 255)
PREVIEW_COLOR = (192, 192, 192)
HIGHLIGHT_COlOR = (255, 255, 0)
POINT_RADIUS = 5
points = []

FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    mouse_pos = pygame.mouse.get_pos()
    closest_point = get_clossest_point(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if closest_point:
                if event.button == 1:
                    points.append(event.pos)
                    print(points)
                elif event.button == 3:
                    remove_point(event.pos)
            elif event.button == 1:
                points.append(event.pos)

    screen.fill(BACKGROUND)

    for i in range(len(points) - 1):
        start_point = points[i]
        end_point = points[i+1]
        pygame.draw.line(screen, LINE_COLOR, start_point, end_point, 3)
    if len(points) > 0:
        mouse_pos = pygame.mouse.get_pos()
        last_point = points[-1]
        pygame.draw.aaline(screen, PREVIEW_COLOR, last_point, mouse_pos, 2)

    if closest_point:
        pygame.draw.circle(screen, HIGHLIGHT_COlOR, closest_point, POINT_RADIUS)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
