import sys

import pygame

from character import Character

from ball import Ball

from random import randint

def check_keydown_event(event, character):
	if event.key == pygame.K_RIGHT:
		character.moving_right = True
	elif event.key == pygame.K_LEFT:
		character.moving_left = True
	elif event.key == pygame.K_UP:
		character.moving_up = True
	elif event.key == pygame.K_DOWN:
		character.moving_down = True
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_event(event, character):
	if event.key == pygame.K_RIGHT:
		character.moving_right = False
	elif event.key == pygame.K_LEFT:
		character.moving_left = False
	elif event.key == pygame.K_UP:
		character.moving_up = False
	elif event.key == pygame.K_DOWN:
		character.moving_down = False

def check_events(character):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event, character)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event, character)

def update_screen(ai_settings, screen, character, balls):
	screen.fill(ai_settings.bg_color)
	character.blitme()
	balls.draw(screen)
	pygame.display.flip()

def get_number_balls_x(ai_settings, ball_width):
	available_space_x = ai_settings.screen_width - ball_width*2
	number_ball_x = int(available_space_x/(ball_width*2))

	return number_ball_x

def get_number_rows(ai_settings, character_height, ball_height):
	available_space_y = ai_settings.screen_height - (ball_height*3 + character_height)
	number_rows = int(available_space_y/(ball_height*2))

	return number_rows

def create_ball(ai_settings, screen, balls, ball_number, ball_row):
	ball = Ball(ai_settings, screen)
	ball_width = ball.rect.width
	random_number = randint(-10, 10)

	ball.x = ball_width + ball_width*2*ball_number
	ball.rect.x = ball.x*random_number
	ball.rect.y = (ball.rect.height + ball.rect.height*2*ball_row)*random_number
	balls.add(ball)

def create_balls(ai_settings, screen, character, balls):
	ball = Ball(ai_settings, screen)
	number_ball_x = get_number_balls_x(ai_settings, ball.rect.width)
	number_rows = get_number_rows(ai_settings, character.rect.height, ball.rect.height)

	for row_number in range(number_rows):
		for ball_number in range(number_ball_x):
			create_ball(ai_settings, screen, balls, ball_number, row_number)

def check_balls_edges(ai_settings, balls):
	for ball in balls.sprites():
		if ball.check_edges():
			change_balls_direction(ai_settings, balls)
			break

def change_balls_direction(ai_settings, balls):
	for ball in balls.sprites():
		ball.rect.y += ai_settings.balls_drop_speed
	ai_settings.balls_direction *= -1

def update_balls(ai_settings, screen, character, balls):
	check_balls_edges(ai_settings, balls)
	balls.update()
	check_character_ball_collisions(ai_settings, screen, character, balls)

	if len(balls) == 0:
		create_balls(ai_settings, screen, character, balls)

def check_character_ball_collisions(ai_settings, screen, character, balls):
	collisions = pygame.sprite.spritecollide(character, balls, True)





























