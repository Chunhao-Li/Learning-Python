import sys

import pygame

from settings import Settings 
from ship import Ship

def run_game():
	#Initiates the game and creats a screen object
	pygame.init()
	ai_settings = Settings()

	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")


	# Create a ship
	ship = Ship(screen)

	# # Set the background colour
	# bg_color = (200,200,200)


	#Start the main loop of the game
	while True:

		#Monitor the keyboard and mouse
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


		screen.fill(ai_settings.bg_color)
		ship.blitme()


		#To display the latest screen
		pygame.display.flip()


run_game()