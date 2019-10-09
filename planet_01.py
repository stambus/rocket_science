import pygame
import math
import os

from planet import Planet

class Planet_01(Planet):
    planet_names = []
    for i in os.listdir('D:\\ZYBA\\Pyth\\test_game\\assets\\Planets'):
        if '.png' in i:
            planet_names.append(i)
    imgs = [pygame.image.load(os.path.join('assets\\Planets\\', str(i))) for i in planet_names]