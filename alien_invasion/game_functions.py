import sys

import pygame

def check_events():
    """Respond to the events of mouse and keyboard"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship, model):
    """Update the surface of the screen, and switch to the new screen"""
    # Initialize the screen after every loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    model.blitme()
    # print(type(model))
    # To reveal the new screen
    pygame.display.flip()