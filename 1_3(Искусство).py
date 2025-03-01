import random
from all_colors import *
import pygame
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('resours/La La Land.mp3')
pygame.mixer.music.play(-1)

size = (0, 0)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption('Искусство')
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
        x = random.randint(0, 1280)
        y = random.randint(0, 1000)
        pygame.draw.circle(screen, color, (x, y), random.randint(1, 100))

    pygame.display.update()
    screen.fill(color)
    pygame.time.delay(random.randint(200, 800))

pygame.quit()
