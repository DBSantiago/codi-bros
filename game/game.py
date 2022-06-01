import random
import sys
import pygame

from .config import *
from .platform import Platform
from .player import Player
from .wall import Wall
from .coin import Coin


class Game:

    def __init__(self):
        pygame.init()

        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        self.running = True
        self.playing = True

        self.clock = pygame.time.Clock()

    def start(self):
        self.new()

    def new(self):
        self.generate_elements()
        self.run()

    def generate_elements(self):
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top - 200)

        self.walls = pygame.sprite.Group()

        self.coins = pygame.sprite.Group()

        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.platform)
        self.sprites.add(self.player)

        self.generate_walls()
        self.generate_coins()

    def generate_walls(self):

        last_position = SCREEN_WIDTH + 100

        if not len(self.walls) > 0:
            for _ in range(0, MAX_WALLS):
                left = random.randrange(last_position + 200, last_position + 400)
                wall = Wall(left, self.platform.rect.top)

                last_position = wall.rect.right

                self.sprites.add(wall)
                self.walls.add(wall)

    def generate_coins(self):
        last_position = SCREEN_WIDTH + 100

        if not len(self.coins) > 0:
            for _ in range(0, MAX_COINS):
                pos_x = random.randrange(last_position + 180, last_position + 300)

                coin = Coin(pos_x, 150)

                last_position = coin.rect.right

                self.sprites.add(coin)
                self.coins.add(coin)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
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
        if self.playing:
            pygame.display.flip()
            pygame.time.delay(20)

            wall = self.player.collide_width(self.walls)
            if wall:
                if self.player.collide_bottom(wall):
                    self.player.skid(wall)
                else:
                    self.stop()

            self.sprites.update()

            self.player.validate_platform(self.platform)

            self.update_elements(self.walls)
            self.generate_walls()
            self.generate_coins()

    def update_elements(self, elements):
        for element in elements:
            if not element.rect.right > 0:
                element.kill()

    def stop(self):
        self.player.stop()
        self.stop_elements(self.walls)

        self.playing = False

    def stop_elements(self, elements):
        for element in elements:
            element.stop()
