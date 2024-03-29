import pygame

from pygame.sprite import Sprite

class Character(Sprite):
	
	def __init__(self, ai_settings, screen):
		super(Character, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load('images/character.gif')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.center = float(self.rect.centerx)
		self.y = float(self.rect.y)

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.character_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.character_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.y -= self.ai_settings.character_speed_factor
		if self.moving_down and self.rect.bottom < 800:
			self.y += self.ai_settings.character_speed_factor

		self.rect.centerx = self.center
		self.rect.y = self.y

	def blitme(self):
		self.screen.blit(self.image, self.rect)

