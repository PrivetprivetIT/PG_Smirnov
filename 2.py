import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

object_pos = [100, 100]
object_pos2 = [100, 400]
object_speed = 5
delay_start_time = 0
delay_duration = 1000  # 1 секунда в миллисекундах
is_delayed = False

running = True
while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_delayed:
                is_delayed = True
                delay_start_time = current_time

    # Проверяем, закончилась ли задержка
    if is_delayed and current_time - delay_start_time > delay_duration:
        is_delayed = False

    if not is_delayed:
        object_pos[0] += object_speed

    object_pos2[0] += object_speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (object_pos[0], object_pos[1], 50, 50))
    pygame.draw.rect(screen, (255, 0, 0), (object_pos2[0], object_pos2[1], 50, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()