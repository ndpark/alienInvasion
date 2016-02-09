#! python3
# alien.py - Sprite for alien in the game

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self, aiSettings, screen):
		super(Alien,self).__init__()
		self.screen = screen
		self.aiSettings = aiSettings
		
		#Loading image and setting it as rect
		self.image = pygame.image.load('alien.bmp')
		self.rect = self.image.get_rect()
		
		#Alien is gonna start top left
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		self.x = float(self.rect.x)
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
	def update(self):
		"""Move alien right"""
		self.x += (self.aiSettings.alienSpeed * self.aiSettings.fleetDirection)
		self.rect.x = self.x
		
	def checkEdges(self):
		"""If alien hits the edge returns true"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
			

