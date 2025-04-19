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

rectangles = []
dragging = False
a = False

FPS = 60
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            top_left = event.pos
            size = 0, 0
            dragging = True

        elif event.type == pygame.MOUSEMOTION and dragging:
            right_bottom = event.pos
            size = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])

        elif event.type == pygame.MOUSEBUTTONUP:
            right_bottom = event.pos
            size = (right_bottom[0] - top_left[0], right_bottom[1] - top_left[1])
            dragging = False
            rect = pygame.Rect(top_left, size)
            rectangles.append((rect, brush_color))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if a:
                    a = False
                else:
                    a = True


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



    screen.blit(canvas, (0, 0))
    draw_palette()

    for rectangle, color in rectangles:
        if a:
            pygame.draw.rect(screen, color, rectangle)
        else:
            pygame.draw.rect(screen, color, rectangle, 1 )

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
