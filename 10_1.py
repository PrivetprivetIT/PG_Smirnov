import random
import os
import pygame
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя игра')
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

pictures = os.listdir('pictures')
picture = random.choice(pictures)
image = pygame.image.load('pictures/' + picture)

ROWS = 3
COLS = 3
MARGIN = 2

image_width, image_height = image.get_size()
tile_width = image_width // COLS
tile_height = image_height // ROWS

tiles = []
for i in range(ROWS):
    for j in range(COLS):
        rect = pygame.Rect(j * tile_width, i * tile_height, tile_width, tile_height)
        tile = image.subsurface(rect)
        tiles.append(tile)

FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)

    screen.blit(image, (0, 0))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
