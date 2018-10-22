import pygame
from ship import Ship

class Doraemon(Ship):
    def __init__(self, screen):
        """Initiate model Doraemon"""
        self.screen = screen

        # Load the doraemon image and get its rect
        self.image = pygame.image.load('images/doraemon.bmp')
        # print(type(self.image))
        # self.image.fill((230, 230, 230))
        self.rect = self.image.get_rect()
        # print(type(self.rect))
        self.screen_rect = screen.get_rect()

        # Put the new shape into the center of the screen
        self.rect.center = self.screen_rect.center


