import pygame
from pygame.locals import *

class Game:
    def __init__(self, width, height):
        self.width = 1000
        self.height = 700
        self.window = pygame.display.set_mode((self.width, self.height))
        pass

    def run(self):
        run =  True
        while run:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    run = False