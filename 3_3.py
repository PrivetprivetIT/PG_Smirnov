from pygame.constants import *
from all_colors import *
import pygame.mixer
pygame.mixer.init()
import pygame
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя игра')
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

pygame.mixer.music.load('resours/sonar.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

shot_sound = pygame.mixer.Sound('resours/shot.mp3')
explosion_sound = pygame.mixer.Sound('resours/explosion.mp3')

volume = 0.5
shot_sound.set_volume(volume)
explosion_sound.set_volume(volume)

FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                shot_sound.play()
            elif event.key == pygame.K_b:
                explosion_sound.play()

            if event.key == pygame.K_UP:
                volume += 0.1
                volume = min(volume, 1)
                shot_sound.set_volume(volume)
                explosion_sound.set_volume(volume)

            elif event.key == pygame.K_DOWN:
                volume -= 0.1
                volume = max(volume, 1)
                shot_sound.set_volume(volume)
                explosion_sound.set_volume(volume)



    screen.fill(BACKGROUND)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
