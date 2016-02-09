import pygame

class Ship():
	def __init__(self, aiSettings, screen):
		self.screen = screen
		self.aiSettings = aiSettings
		#Loads image of the ship
		self.image = pygame.image.load('ship.bmp')
		
		#Load rect attibute (treats it as rectangle)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#New ship at the bottom & sets location for the ship
		self.rect.centery = self.screen_rect.centery
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#Store decimal value for ship's center
		self.centery = float(self.rect.centery)
		self.centerx = float(self.rect.centerx)

		
		
		#Movement
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
		
		
	#Updates the ship based on flag conditions
	def update(self):
	#Updates center value
		#Movement limits/ movement 
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.aiSettings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.aiSettings.ship_speed_factor
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.centery -= self.aiSettings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom :
			self.centery += self.aiSettings.ship_speed_factor
			
		self.rect.centerx=self.centerx
		self.rect.centery = self.centery
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		
	def centerShip(self):
		self.centerx = self.screen_rect.centerx
		self.centery = self.screen_rect.bottom