import pygame
import math
import os
import random


class Planet:
    imgs = []

    def __init__(self):
        self.radius = random.randrange(96, 96 * 2)
        self.x = random.randrange(self.radius + 50, 1000 - self.radius)
        self.y = random.randrange(self.radius + 50, 700 - self.radius)
        self.selected = False
        self.img = pygame.transform.scale(random.choice(self.imgs), (self.radius, self.radius))

    def draw(self, window):
        """
        Draws rocket with an image
        :param window: surface
        :return: None
        """
        window.blit(self.img, (self.x, self.y))

    def click(self, X, Y):
        """
        Returns if planet has been clicked on,
        and selects it.
        :param X: int
        :param Y: int
        :return: Bool
        """
        if X <= self.x + self.radius and X >= self.x:
            if Y <= self.y + self.radius and Y >= self.y:
                return True
        return False
