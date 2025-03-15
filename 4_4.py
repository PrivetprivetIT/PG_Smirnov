from all_colors import *
import pygame
pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя игра')
BACKGROUND = YELLOW
screen.fill(BACKGROUND)

my_font = pygame.font.SysFont('Arial', 32)
my_text = my_font.render('Потрачено!', True, (0, 0, 0), (BACKGROUND))
screen.blit(my_text, (100, 100))

FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
