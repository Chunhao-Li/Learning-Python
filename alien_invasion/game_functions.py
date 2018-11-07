import sys

import pygame

def check_events(ship):
    """Respond to the events of mouse and keyboard"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # move the ship to the right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    """Update the surface of the screen, and switch to the new screen"""
    # Initialize the screen after every loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # model.blitme()
    # print(type(model))
    # To reveal the new screen
    pygame.display.flip()