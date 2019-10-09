import pygame
import math
import os
import random


class Planet:
    imgs = []

    def __init__(self):
        self.img = random.choice(self.imgs)
        self.radius = random.randrange(96, 96 * 2)
        self.x = random.randrange(self.radius + 50, 1000 - self.radius)
        self.y = random.randrange(self.radius + 50, 700 - self.radius)

    def draw(self, window):
        """
        Draws rocket with an image
        :param window: surface
        :return: None
        """
        self.img = pygame.transform.scale(self.img, (self.radius, self.radius))
        window.blit(self.img, (self.x, self.y))

    def collide(self, X, Y):
        """
        Returns if position has hit an object (sky, ground)
        :param X:
        :param Y:
        :return: Bool
        """
        if X <= self.x + self.radius and X >= self.x:
            if Y <= self.y + self.radius and Y >= self.y:
                return True
        return False
