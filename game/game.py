import random
import sys
import pygame
import os

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

        self.clock = pygame.time.Clock()

        self.dir = os.path.dirname(__file__)
        self.dir_sounds = os.path.join(self.dir, "assets/sounds")
        self.dir_sprites = os.path.join(self.dir, "assets/sprites")
        self.dir_fonts = os.path.join(self.dir, "assets/fonts")

        self.font = pygame.font.match_font("RussoOne-Regular.ttf")

        pygame.mixer.music.load(os.path.join(self.dir_sounds, "rising_tide_-_antarctica.xm"))
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1, 0.0)

    def start(self):
        self.menu()
        self.new()

    def new(self):
        self.playing = True
        self.score = 0
        self.level = 0
        self.background = pygame.image.load(os.path.join(self.dir_sprites, "codi_bros_bg.png"))
        self.generate_elements()
        self.run()

    def generate_elements(self):
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top - 200, self.dir_sprites)

        self.walls = pygame.sprite.Group()

        self.coins = pygame.sprite.Group()

        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.platform)
        self.sprites.add(self.player)

        self.generate_walls()

    def generate_walls(self):

        last_position = SCREEN_WIDTH + 100

        if not len(self.walls) > 0:
            for _ in range(0, MAX_WALLS):
                left = random.randrange(last_position + 200, last_position + 400)
                wall = Wall(left, self.platform.rect.top, self.dir_sprites)

                last_position = wall.rect.right

                self.sprites.add(wall)
                self.walls.add(wall)

            self.level += 1
            self.generate_coins()

    def generate_coins(self):
        last_position = SCREEN_WIDTH + 100

        for _ in range(0, MAX_COINS):
            pos_x = random.randrange(last_position + 180, last_position + 300)

            coin = Coin(pos_x, 120, self.dir_sprites)

            last_position = coin.rect.right

            self.sprites.add(coin)
            self.coins.add(coin)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_SPACE] or pressed_key[pygame.K_UP]:
            self.player.jump()

        if pressed_key[pygame.K_r] and not self.playing:
            self.new()

    def draw(self):
        self.surface.blit(self.background, (0, 0))

        self.draw_text()

        self.sprites.draw(self.surface)

        pygame.display.flip()

    def update(self):
        if not self.playing:
            return

        pygame.time.delay(20)

        wall = self.player.collide_width(self.walls)
        if wall:
            if self.player.collide_bottom(wall):
                self.player.skid(wall)
            else:
                self.stop()

        coin = self.player.collide_width(self.coins)
        if coin:
            coin_sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, "codi_bros_coin_sound.wav"))
            coin_sound.play()
            coin.kill()
            self.score += 1

        self.sprites.update()

        self.player.validate_platform(self.platform)

        self.update_elements(self.walls)
        self.generate_walls()

    def update_elements(self, elements):
        for element in elements:
            if not element.rect.right > 0:
                element.kill()

    def stop(self):
        self.player.stop()
        self.stop_elements(self.walls)

        lose_sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, "codi_bros_lose.wav"))
        lose_sound.play()

        self.playing = False

    def stop_elements(self, elements):
        for element in elements:
            element.stop()

    def display_text(self, text, size, color, pos_x, pos_y):
        font = pygame.font.Font(self.font, size)

        text = font.render(text, True, color)
        rect = text.get_rect()
        rect.midtop = (pos_x, pos_y)

        self.surface.blit(text, rect)

    def draw_text(self):
        self.display_text(self.score_format(), 36, GREEN, SCREEN_WIDTH * 0.875, 20)
        self.display_text(self.level_format(), 36, GREEN, SCREEN_WIDTH * 0.125, 20)

        if not self.playing:
            self.display_text("Perdiste!  =(", 60, RED_STRONG, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            self.display_text("Presiona R para comenzar de nuevo", 30, RED_STRONG, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.25)

    def score_format(self):
        return f"SCORE: {self.score}"

    def level_format(self):
        return f"LEVEL {self.level}"

    def menu(self):
        self.surface.fill(GREEN_LIGHT)
        self.display_text("Presiona una tecla para comenzar", 48, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        pygame.display.flip()

        self.wait()

    def wait(self):
        wait = True

        while wait:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYUP:
                    wait = False
