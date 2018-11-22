# coding=utf-8
import sys

import pygame


def check_keydown_events(event, ship):
    """ Respond to the key press"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """ Respond to the key release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """ Respond to the keyboards and mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """Update the surface of the screen, and switch to the new screen"""
    # Initialize the screen after every loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # model.blitme()
    # print(type(model))
    # To reveal the new screen
    pygame.display.flip()
