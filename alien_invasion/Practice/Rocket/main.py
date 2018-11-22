import pygame

from rocket import Rocket
import game_functions as gf 
from settings import Settings

def run_game():
  pygame.init()
  ai_settings = Settings()

  screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption("Rocket Game")

  rocket = Rocket(ai_settings, screen)

  while True:

    gf.check_events(rocket)
    rocket.update()
    gf.update_screen(ai_settings, screen, rocket)


run_game()