import pygame

from settings import Settings 
from ship import Ship
import game_functions as gf
from model import Doraemon

def run_game():
    #Initiates the game and creats a screen object
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    # Create a ship
    ship = Ship(ai_settings, screen)

    # Create a model
    # doraemon = Doraemon(screen)

    # # Set the background colour
    # bg_color = (200,200,200)


    #Start the main loop of the game
    while True:

        #Monitor the keyboard and mouse
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)





run_game()