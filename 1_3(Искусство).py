import random
from all_colors import *
import pygame
pygame.init()

#pygame.mixer.init()
#pygame.mixer.musik.load('resours/LA la land.mp3')
#pygame.mixer.musik.play(-1)

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя игра')
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    for i in range(10):
        color = random.choice(colors)
        x = random.randint(0, size[0])
        y = random.randint(0, size[1])
        pygame.draw.circle(screen, color, (x, y), random.randint(1, 100))

    pygame.display.update()
    screen.fill(color)
    pygame.time.delay(random.randint(200, 800))

pygame.quit()
