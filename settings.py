#! python3
# settings.py

class Settings():
	"""Static settings"""
	def __init__(self):
		self.screen_width=1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		
		self.shipLimit = 3
		
		#Bullet settings
		self.bulletWidth = 3
		self.bulletHeight = 15
		self.bulletColor = (60,60,60)
		self.bulletsAllowed = 8
		
		#Game speeding up
		self.speedupScale = 1.1
		self.scoreScale = 1.5
		
		self.initializeDynamicSettings()
		
		#Score!
		self.alienPoints = 50
		
	def initializeDynamicSettings(self):
		"""Dynamic settings as game continues"""
		
		self.ship_speed_factor = 1.5
		self.bulletSpeedFactor = 3
		self.alienSpeed = 1
		self.fleetDropSpeed = 10
		self.fleetDirection = 1
		
		#This can be used to make speed ups 
	def increaseSpeed(self):
		"""Increase speed settings"""
		self.ship_speed_factor *= self.speedupScale
		self.bulletSpeedFactor *= self.speedupScale
		self.alienSpeed *= self.speedupScale
		
		self.alienPoints = int(self.alienPoints * self.scoreScale)
		
	
		