import pygame

from .config import PLAYER_GRAVITY, PLAYER_HEIGHT, PLAYER_WIDTH, BLUE


class Player(pygame.sprite.Sprite):

    def __init__(self, left, bottom):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        self.pos_y = self.rect.bottom
        self.vel_y = 0

    def validate_platform(self, platform):
        collision = pygame.sprite.collide_rect(self, platform)

        if collision:
            self.vel_y = 0
            self.pos_y = platform.rect.top

    def update_pos(self):
        self.vel_y += PLAYER_GRAVITY
        self.pos_y += self.vel_y + 0.5 * PLAYER_GRAVITY

    def update(self):
        self.update_pos()

        self.rect.bottom = self.pos_y
