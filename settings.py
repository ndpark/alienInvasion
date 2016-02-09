#! python3
# settings.py

class Settings():
	def __init__(self):
		self.screen_width=1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		self.ship_speed_factor = 1.5
		self.alienSpeed = 1
		self.fleetDropSpeed = 10
		self.fleetDirection = 1
		self.shipLimit = 3
		
		#Bullet settings
		self.bulletSpeedFactor = 3
		self.bulletWidth = 3
		self.bulletHeight = 15
		self.bulletColor = (60,60,60)
		self.bulletsAllowed = 8