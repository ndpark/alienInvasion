import pygame.font

class Button():
	def __init__(self, aiSettings, screen, msg):
		self.screen = screen
		self.screenRect = screen.get_rect()
		
		#Properties of button
		self.width, self.height = 200,50
		self.buttonColor = (0,255,0)
		self.textColor = (255,255,255)
		self.font = pygame.font.SysFont(None, 48)
		
		self.rect = pygame.Rect(0,0,self.width, self.height)
		self.rect.center = self.screenRect.center
		
		self.prepMsg(msg)
		
	def prepMsg(self, msg):
		"""Turn msg into img"""
		self.msgImage = self.font.render(msg, True, self.textColor, self.buttonColor)
		self.msgImageRect = self.msgImage.get_rect()
		self.msgImageRect.center = self.rect.center
		
	def drawButton(self):
		"""Draws a buttton and write messege"""
		self.screen.fill(self.buttonColor, self.rect)
		self.screen.blit(self.msgImage, self.msgImageRect)
		