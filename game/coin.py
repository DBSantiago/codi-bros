import pygame

from .config import COIN_WIDTH, COIN_HEIGHT, COIN_SPEED, YELLOW


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((COIN_WIDTH, COIN_HEIGHT))
        self.image.fill(YELLOW)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

        self.vel_x = COIN_SPEED

    def update(self):
        self.rect.left -= self.vel_x

    def stop(self):
        self.vel_x = 0
