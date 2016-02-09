class GameStats():
	def __init__(self, aiSettings):
		"""Initialize stats"""
		self.aiSettings = aiSettings
		self.resetStats()
		self.game_active = False
		
	def resetStats(self):
		"""Initialize stats that changes during the game"""
		self.shipsLeft = self.aiSettings.shipLimit
		
	