import sys

import pygame

def check_events(rocket):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
      if event.key == pygame.K_LEFT:
        rocket.moving_left = True

    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
      if event.key == pygame.K_LEFT:
        rocket.moving_left = False


def update_screen(ai_settings, screen, rocket):

  screen.fill(ai_settings.bg_color)
  rocket.blitme()
  pygame.display.flip()