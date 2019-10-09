import pygame
import math
import os

from rocket import Rocket


class Rocket_01(Rocket):
    rocket_names = os.listdir('D:\\ZYBA\\Pyth\\test_game\\assets\\Rockets\\Spaceships\\01')
    imgs = [pygame.image.load(os.path.join('assets\\Rockets\\Spaceships\\01', str(i))) for i in rocket_names]


