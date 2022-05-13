import pygame

from .config import PLAYER_HEIGHT, PLAYER_WIDTH, BLUE


class Player(pygame.sprite.Sprite):
    def __init__(self, left, bottom):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom
