import sys
import pygame


def Game():

    def __init__(self):
        pygame.init()

        width = 800
        height = 400
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Codi Bros")

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
