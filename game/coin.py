import pygame
import os

from .config import COIN_WIDTH, COIN_HEIGHT, COIN_SPEED


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, dir_sprites):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join(dir_sprites, "codi_bros_coin.png"))

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

        self.vel_x = COIN_SPEED

    def update(self):
        self.rect.left -= self.vel_x

    def stop(self):
        self.vel_x = 0
