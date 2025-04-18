def draw_palette():
    palette.fill(BACKGROUND)

    for i in range(12):
        color_rect = pygame.Rect(i * size, 0, size, size)
        pygame.draw.rect(palette, COLORS[i], color_rect)

    border_rect = pygame.Rect(CUR_INDEX * size, 0, size, size)
    pygame.draw.rect(palette, BORDER_COLOR, border_rect, width=3)

    screen.blit(palette, palette_rect.topleft)

from all_colors import COLORS
import random
import pygame
pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя игра')
BACKGROUND = (255, 255, 255)

brush_color = (0, 0, 0)
brush_width = 5

BORDER_COLOR = (0, 0, 0)
CUR_INDEX = 0

canvas = pygame.Surface(screen.get_size())
canvas.fill(BACKGROUND)

size = 50
palette_rect = pygame.Rect(10, 10, 12*size, 50)
palette = pygame.Surface(palette_rect.size)

dragging_palette = False

FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if palette_rect.collidepoint(mouse_pos):
                dragging_palette = True
                offset = (event.pos[0] - palette_rect.left,
                          event.pos[1] - palette_rect.top)
            else:
                dragging_palette = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            dragging_palette = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                brush_width += 1

            elif event.key == pygame.K_DOWN:
                brush_width -= 1
                if brush_width < 0:
                    brush_width = 0

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if mouse_pressed[0]:
        if palette_rect.collidepoint(mouse_pos):
            selected_color_index = ((mouse_pos[0] - palette_rect.left)//size)
            CUR_INDEX = selected_color_index
            brush_color = COLORS[CUR_INDEX]
        else:
            pygame.draw.circle(canvas, brush_color, mouse_pos, brush_width)


    if dragging_palette:
        new_pos = (mouse_pos[0] - offset[0], mouse_pos[1] - offset[1])
        palette_rect.topleft = new_pos

    screen.blit(canvas, (0, 0))
    draw_palette()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
