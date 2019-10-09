import pygame
import math
import os


class Rocket:
    imgs = []

    def __init__(self):
        self.x = 10
        self.y = 10
        self.fuel = 100
        self.weight = 10000
        self.speed = 3
        self.img = None
        self.width = 64
        self.height = 64

    def fly(self):
        """
        FLy rocket. All the physics goes here
        :return:
        """

    def draw(self, window):
        """
        Draws rocket with an image
        :param window: surface
        :return: None
        """
        self.img = self.imgs[0]
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        window.blit(self.img, (self.x, self.y))

    def collide(self, X, Y):
        """
        Returns if position has hit an object (sky, ground)
        :param X:
        :param Y:
        :return: Bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False
