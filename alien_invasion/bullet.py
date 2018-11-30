import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ The class which manages the bullets. """
    def __init__(self, ai_settings, screen, ship):
        """ Create a bullet object at the position of the ship"""
        super().__init__()