import pygame

class Rocket():

  def __init__(self, ai_settings, screen):
    """ Initiate the rocket"""
    self.screen = screen
    # self.ai_settings = ai_settings

    # load the image and get its rect
    self.image = pygame.i mage.load('image/rocket.bmp')
    self.rect = self.image.get_rect()

    # get the screen rect
    self.screen_rect = screen.get_rect()

    # put the rocket at the bottom centre
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

    # moving signal
    self.moving_right = False
    self.moving_left = False

  def update(self):
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.rect.centerx += 20

    if self.moving_left and self.rect.left > 0:
      self.rect.centerx -= 20


  def blitme(self):
    self.screen.blit(self.image, self.rect)