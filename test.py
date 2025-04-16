import random
import time

import pygame
pygame.init()

pacman_images = {"up": pygame.image.load("resours/pacman_up.png"), "down": pygame.image.load("resours/pacman_down.png"),
                 "left": pygame.image.load("resours/pacman_left.png"),
                 "right": pygame.image.load("resours/pacman_right.png"),
                 "up_left": pygame.image.load("resours/pacman_up_left.png"),
                 "up_right": pygame.image.load("resours/pacman_up_right.png"),
                 "down_left": pygame.image.load("resours/pacman_down_left.png"),
                 "down_right": pygame.image.load("resours/pacman_down_right.png")}

ghost_images = {"red": pygame.image.load("resours/red_ghost.png"), "pink": pygame.image.load("resours/pink_ghost.png"),
                "blue": pygame.image.load("resours/blue_ghost.png"),
                "orange": pygame.image.load("resours/orange_ghost.png")}


def get_direction (pos1, pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    direction = "right"

    if dy < 0:
        if dx < 0:
            direction = "up_left"
        elif dx > 0:
            direction = "up_right"
        else:
            direction = "up"


    elif dy > 0:
        if dx < 0:
            direction = "down_left"
        elif dx > 0:
            direction = "down_right"
        else:
            direction = "down"

    else:
        if dx < 0:
            direction = "left"
        elif dx > 0:
            direction = "right"

    return direction


def move_towards(pos1, pos2, speed):
    x1, y1 = pos1
    x2, y2 = pos2
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > speed:
        if dx > 0:
            x1 += speed
        else:
            x1 -= speed
    else:
        x1 = x2

    if abs (dy) > speed:
        if dy > 0:
            y1 += speed
        else:
            y1 -= speed
    else:
        y1 = y2


    return (x1, y1)

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pac-Man смотрит на курсор")

BACKGROUND = (0, 0, 0)

pacman_pos = (400, 300)
speed = 4

clock = pygame.time.Clock()
FPS = 60

# Переменные для управления призраками
ghost_spawn_time = 0
ghost_duration = 5  # секунды
current_ghost_pos = None
current_ghost_color = None

running = True

while running:
    current_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()

    direction = get_direction(pacman_pos, mouse_pos)
    pacman_pos = move_towards(pacman_pos, mouse_pos, speed)

    # Проверяем, нужно ли создать нового призрака
    if current_time - ghost_spawn_time >= ghost_duration:
        current_ghost_pos = (random.randint(0, size[0] - 50), random.randint(0, size[1] - 50))
        current_ghost_color = random.choice(list(ghost_images.keys()))
        ghost_spawn_time = current_time


    screen.fill(BACKGROUND)

        # Рисуем Пакмана
    pacman_image = pacman_images[direction]
    screen.blit(pacman_image, pacman_pos)

        # Рисуем призрака, если он активен (время еще не истекло)
    if current_ghost_pos and (current_time - ghost_spawn_time < ghost_duration):
        ghost_image = ghost_images[current_ghost_color]
    screen.blit(ghost_image, current_ghost_pos)


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()