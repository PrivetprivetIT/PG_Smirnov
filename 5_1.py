# добавить звуки, скорость отобразить и ограничить до 30

import sys

from all_colors import *
from pygame.constants import *
import pygame
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Пинг понг')
BACKGROUND = BLACK
screen.fill(BACKGROUND)

PADDLE_WIDTH = 25
PADDLE_HEIGHT = 100
PADDLE_SPEED = 10

BALL_SIZE = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

paddle_rect = pygame.Rect(0, size[1] // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH,
                          PADDLE_HEIGHT)

paddle_rect1 = pygame.Rect(size[0] - PADDLE_WIDTH, size[1] // 2 - PADDLE_HEIGHT // 2,
                          PADDLE_WIDTH, PADDLE_HEIGHT)

ball_rect = pygame.Rect(size[0] // 2 - BALL_SIZE // 2, size[1] // 2 - BALL_SIZE // 2,
                        BALL_SIZE, BALL_SIZE)

score1 = 0
score2 = 0

font = pygame.font.SysFont(None, 48)

ai_mode = True

if len(sys.argv) > 1:
    if sys.argv[1] == '--human':
        ai_mode = False

def update_ai():
    if ball_rect.x > size[0] // 2:
        if ball_rect.centery < paddle_rect1.centery:
            paddle_rect1.y -= PADDLE_SPEED
        elif ball_rect.centery > paddle_rect1 .centery:
            paddle_rect1.y += PADDLE_SPEED

        if paddle_rect1.top < 0:
            paddle_rect1.top = 0
        if paddle_rect.bottom > size[1]:
            paddle_rect1.bottom = size[1]

    else:
        paddle_rect1.centery += (size[1] // 2 - paddle_rect1.centery) / PADDLE_SPEED

FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_w]:
        paddle_rect.y -= PADDLE_SPEED
    if keys[K_s]:
        paddle_rect.y += PADDLE_SPEED
    if keys[K_UP]:
        paddle_rect1.y -= PADDLE_SPEED
    if keys[K_DOWN]:
        paddle_rect1.y += PADDLE_SPEED

    if paddle_rect.y < 0:
        paddle_rect.y = 0
    if paddle_rect.y > size[1] - PADDLE_HEIGHT:
        paddle_rect.y = size[1] - PADDLE_HEIGHT
    if paddle_rect1.y < 0:
        paddle_rect1.y = 0
    if paddle_rect1.y > size[1] - PADDLE_HEIGHT:
        paddle_rect1.y = size[1] - PADDLE_HEIGHT

    if ai_mode:
        update_ai()

    ball_rect.x += BALL_SPEED_X
    ball_rect.y += BALL_SPEED_Y

    if ball_rect.top < 0:
        BALL_SPEED_Y = - BALL_SPEED_Y
    if ball_rect.bottom > 720:
        BALL_SPEED_Y = - BALL_SPEED_Y

    if ball_rect.colliderect(paddle_rect) or ball_rect.colliderect(paddle_rect1):
        BALL_SPEED_X = - BALL_SPEED_X
        BALL_SPEED_X *= 1.1
        BALL_SPEED_Y *= 1.1

    if ball_rect.left <= 0:
        ball_rect.center = (size[0] // 2, size[1] // 2)
        BALL_SPEED_X = BALL_SPEED_Y = 5
        score2 += 1

    if ball_rect.x > size[0]:
        ball_rect.center = (size[0] // 2, size[1] // 2)
        BALL_SPEED_X = BALL_SPEED_Y = 5
        score1 += 1

    screen.fill(BACKGROUND)

    pygame.draw.rect(screen, WHITE, paddle_rect)
    pygame.draw.rect(screen, WHITE, paddle_rect1)
    pygame.draw.rect(screen, WHITE, ball_rect)
    pygame.draw.line(screen, WHITE, (size[0] // 2, 0), (size[0] // 2, size[1]), 1)

    if score1 == 3:
        BALL_SPEED_X = 0
        BALL_SPEED_Y = 0
        score_text = font.render(f'Первый игрок победил', True, WHITE)
    elif score2 == 3:
        BALL_SPEED_X = 0
        BALL_SPEED_Y = 0
        score_text = font.render(f'Второй игрок победил', True, WHITE)
    else:
        score_text = font.render(f'{score1} : {score2}', True, WHITE)

    screen.blit(score_text, (size[0] // 2 - score_text.get_width() // 2, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
