from pygame.constants import *
import pygame
pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя игра')
BACKGROUND = pygame.image.load('resours/sky.jpg')

plane1 = pygame.image.load('resours/plane1.png')
plane2 = pygame.image.load('resours/plane2.png')

speed = 5
x, y = 50, 50
pos = (400, 400)
FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()


    keys = pygame.key.get_pressed()

    if keys[K_LEFT]:
        x -= speed
    if keys[K_RIGHT]:
        x += speed
    if keys[K_UP]:
        y -= speed
    if keys[K_DOWN]:
        y += speed

    if y < -40:
        y = -40
    if y > 440:
        y = 440
    if x < 0:
        x = 0
    if x > 600:
        x = 600



    screen.blit(BACKGROUND, (0, 0))
    screen.blit(plane1, (x, y))
    screen.blit(plane2, (pos[0] - 112, pos[1] - 80))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
