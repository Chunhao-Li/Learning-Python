import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """ initiate the ship and set its original position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # Put the new ship at the bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store float centerx
        self.center = float(self.rect.centerx)

        # moving signal
        self.moving_right = False
        self.moving_left   = False

    def update(self):
        """ TO move the position of ship according to the moving signal"""
        # update the center value instead of rect
        if self.moving_right and self.rect.right < self.screen_rect.right :
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0 :
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor

        # update rect according to self.center
        self.rect.centerx = self.center

    def blitme(self):
        """ Plot the ship in a specific position"""
        self.screen.blit(self.image, self.rect)