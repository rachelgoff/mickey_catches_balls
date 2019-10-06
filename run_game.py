import sys

import pygame

from settings import Settings

from character import Character

import game_function as gf

from pygame.sprite import Group

from ball import Ball

def run_game():

	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	character = Character(ai_settings, screen)
	balls = Group()
	gf.create_balls(ai_settings, screen, character, balls)

	while True:
		gf.check_events(character)
		character.update()
		gf.update_balls(ai_settings, screen, character, balls)
		gf.update_screen(ai_settings, screen, character, balls)

run_game()