import abc
import pygame

pygame.init()
pygame.font.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя игра')
BACKGROUND = (0, 0, 0)
screen.fill(BACKGROUND)

FPS = 60
clock = pygame.time.Clock()

player_name = "Аноним"
font = pygame.font.SysFont(None, 64)

class State(abc.ABC):
    @abc.abstractmethod
    def handle_events(self, events):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def draw(self, screen):
        pass

class SplashScreen(State):
    def __init__(self):
        self.text = "Заставка"
        self.surface = font.render(self.text, True, (255, 255, 255))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        return self

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BACKGROUND)
        rect = self.surface.get_rect()
        rect.center = (size[0] // 2, size[1] // 2)
        screen.blit(self.surface, rect)

state = SplashScreen()

running = True
while running:
    events = pygame.event.get()

    state = state.handle_events(events)
    state.update()
    state.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()