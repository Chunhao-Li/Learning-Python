import pygame

class Ship():

    def __init__(self, screen):
        """ initiate the ship and set its original position"""
        self.screen = screen


        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # Put the new ship at the bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # moving signal
        self.moving_right = False
        self.moving_left   = False

    def update(self):
        """ TO move the position of ship according to the moving signal"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1


    def blitme(self):
        """ Plot the ship in a specific position"""
        self.screen.blit(self.image, self.rect)