# ВЗЯТЬ ЗА ОСНОВУ ИГРОВУЮ МЕХАНИКУ И РАЗРАБОТАТЬ ИГРУ
# ДОБАВИТЬ ОПИСАНИЕ ИГРЫ
import pygame
pygame.init()
# Загружаем изображения Pac-Man'a для каждого направления 7
pacman_images = {"up": pygame.image.load("resours/pacman_up.png"), "down": pygame.image.load("resours/pacman_down.png"),
                 "left": pygame.image.load("resours/pacman_left.png"), "right": pygame.image.load("resours/pacman_right.png"),
                 "up_left": pygame.image.load("resours/pacman_up_left.png"), "up_right": pygame.image.load("resours/pacman_up_right.png"),
                 "down_left": pygame.image.load("resours/pacman_down_left.png"),
                 "down_right": pygame.image.load("resours/pacman_down_right.png") }
# Получить направление движения Pac-Man'a
def get_direction (pos1, pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    direction = "right" # по умолчани
# if abs(dx) < 2 and abs (dy) < 2:
#    return direction # почти не двигается
    if dy < 0: # вверх
        if dx < 0:
            direction = "up_left"
        elif dx > 0:
            direction = "up_right"
        else:
            direction = "up"


    elif dy > 0: #BHU3
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


# Перемещение Рас-Man'a к курсору
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


# Инициализация экрана
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pac-Man смотрит на курсор")

# Цвет фона
BACKGROUND = (0, 0, 0)

# Начальная позиция Pac-Man'a
pacman_pos = (400, 300)
speed = 4

# Игровой цикл
clock = pygame.time.Clock()
FPS = 60


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()

    # Определяем направление и перемещаем Рас-Man'a direction get_direction (pacman_pos, mouse_pos)
    direction = get_direction(pacman_pos, mouse_pos)
    pacman_pos = move_towards (pacman_pos, mouse_pos, speed)

    # Отрисовка
    screen.fill (BACKGROUND)

    pacman_image = pacman_images[direction]
    screen.blit(pacman_image, pacman_pos)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
