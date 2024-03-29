import pygame
from pygame.locals import *
import os
from rocket_01 import Rocket_01
from planet_01 import Planet_01



class Game:
    def __init__(self):
        self.width = 1000
        self.height = 700
        self.window = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load(os.path.join('assets', 'Backgrounds', 'space_bg.jpg'))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.rockets = [Rocket_01()]
        self.planets = [Planet_01()]

    def run(self):
        run = True
        FPS = 60
        clock = pygame.time.Clock()
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
            self.draw()
        pygame.quit()

    def draw(self):
        self.window.blit(self.bg, (0, 0))

        # Draw planets
        for p in self.planets:
            p.draw(self.window)

        # Draw rockets
        for r in self.rockets:
            r.x = p.x + p.radius/2 - r.width/2
            r.y = p.y - r.height/2
            r.draw(self.window)

        pygame.display.update()


game_instance = Game()
game_instance.run()
