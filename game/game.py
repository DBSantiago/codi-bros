import sys
import pygame

from game.config import *


class Game():

    def __init__(self):
        pygame.init()

        width = 800
        height = 400
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        self.running = True

    def start(self):
        self.new()

    def new(self):
        self.run()

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

    def draw(self):
        pass

    def update(self):
        pygame.display.flip()

    def stop(self):
        pass
