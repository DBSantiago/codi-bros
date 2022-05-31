import pygame

from .config import WALL_WIDTH, WALL_HEIGHT, RED, WALL_SPEED


class Wall(pygame.sprite.Sprite):
        def __init__(self, left, bottom):
            pygame.sprite.Sprite.__init__(self)

            self.image = pygame.Surface((WALL_WIDTH, WALL_HEIGHT))
            self.image.fill(RED)

            self.rect = self.image.get_rect()
            self.rect.left = left
            self.rect.bottom = bottom

            self.vel_x = WALL_SPEED

        def update(self):
            self.rect.left -= self.vel_x

        def stop(self):
            self.vel_x = 0
