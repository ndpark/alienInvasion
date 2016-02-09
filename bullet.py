#! pyhon3
# bullets.py

import pygame
from pygame.sprite import Sprite

#Spirite allows elements to be grouped
class Bullet(Sprite):
	"""Bullets!"""
	def __init__(self,aiSettings,screen,ship):
		super(Bullet,self).__init__()
		self.screen = screen
		
		#Create bullet rect at (0,0) then set correct position
		self.rect = pygame.Rect(0,0, aiSettings.bulletWidth, aiSettings.bulletHeight)
		
		#Sets the bullet to look like it shoots at the top of the ship
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		self.y = float(self.rect.y)
		
		self.color = aiSettings.bulletColor
		self.speedFactor = aiSettings.bulletSpeedFactor

	#Move bullet up screen	
	def update(self):
		self.y -= self.speedFactor
		self.rect.y = self.y

	#Draws bullet
	def drawBullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)