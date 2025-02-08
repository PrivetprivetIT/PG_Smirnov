from all_colors import *
import pygame
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Примитивы')
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

line_color = RED
line_width = 5
start_pos = (0, size[1]//2)
end_pos = (size[0], size[1]//2)

FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)

    pygame.draw.line(screen, line_color, start_pos, end_pos, line_width)

    pygame.draw.rect(screen, ORANGE, (50, 50, 100, 100))
    pygame.draw.rect(screen, ORANGE, (250, 50, 100, 100), 5)
    pygame.draw.rect(screen, ORANGE, (450, 50, 100, 100), border_radius = 20)

    pygame.draw.ellipse(screen, ORANGE, (50, 450, 100, 100))
    pygame.draw.ellipse(screen, ORANGE, (250, 450, 100, 100), 5)

    pygame.draw.polygon(screen, ORANGE, ((750, 250), (800, 300), (850, 250)))
    pygame.draw.polygon(screen, ORANGE, ((1000, 200), (1050, 250), (1000, 300)), 5)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
