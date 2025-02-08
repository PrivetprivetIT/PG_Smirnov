import random
from all_colors import *
import pygame
pygame.init()

#pygame.mixer.init()
#pygame.mixer.musik.load('resours/LA la land.mp3')
#pygame.mixer.musik.play(-1)

size = (0, 0)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption('Дискотека')
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

colors = [BLACK, WHITE, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PINK,
          BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, SILVER, GOLD]


clock = pygame.time.Clock()

running = True

timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    color = random.choice(colors)
    screen.fill(color)
    pygame.display.flip()
    pygame.time.delay(random.randint(200, 800))

pygame.quit()
