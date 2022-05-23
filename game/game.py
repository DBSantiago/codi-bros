import sys
import pygame

from .config import *
from .platform import Platform
from .player import Player

clock = pygame.time.Clock()
clock.tick(60)

class Game():

    def __init__(self):
        pygame.init()

        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        self.running = True

    def start(self):
        self.new()

    def new(self):
        self.generate_elements()
        self.run()

    def generate_elements(self):
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top - 200)

        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.platform)
        self.sprites.add(self.player)

    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_SPACE] or pressed_key[pygame.K_UP]:
            self.player.jump()

    def draw(self):
        self.surface.fill(BLACK)
        self.sprites.draw(self.surface)

    def update(self):
        pygame.display.flip()

        self.sprites.update()

        self.player.validate_platform(self.platform)

    def stop(self):
        pass
