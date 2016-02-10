import pygame.font

class Scoreboard():
	"""Contains score"""
	
	def __init__(self, aiSettings, screen, stats):
		"""Score keeping attributes"""
		self.screen = screen
		self.screenRect = screen.get_rect()
		self.aiSettings = aiSettings
		self.stats = stats
		
		#Font
		self.textColor = (30,30,30)
		self.font = pygame.font.SysFont(None, 48)
		
		self.prepScore()
		self.prepHighScore()
		self.prepLevel()
		
	def prepScore(self):
		"""Score into image"""
		roundedScore = int(round(self.stats.score,-1))
		scoreStr = "{:,}".format(roundedScore)
		self.scoreImage = self.font.render(scoreStr, True, self.textColor, self.aiSettings.bg_color)
		
		#Score at top right
		self.scoreRect = self.scoreImage.get_rect()
		self.scoreRect.right = self.screenRect.right - 20
		self.scoreRect.top = 20
		
	def showScore(self):
		"""Score on screen"""
		self.screen.blit(self.scoreImage, self.scoreRect)
		self.screen.blit(self.highScoreImage, self.highScoreRect)
		self.screen.blit(self.levelImage, self.levelRect)
		
	def prepHighScore(self):
		highScore = int(round(self.stats.highScore, -1))
		highScoreStr = "{:,}".format(highScore)
		self.highScoreImage = self.font.render(highScoreStr, True, self.textColor, self.aiSettings.bg_color)
		
		#Center highscore
		self.highScoreRect = self.highScoreImage.get_rect()
		self.highScoreRect.centerx = self.screenRect.centerx
		self.highScoreRect.top = self.scoreRect.top
		
	def prepLevel(self):
		"""Turn elvel into rendered image"""
		self.levelImage = self.font.render(str(self.stats.level), True, self.textColor, self.aiSettings.bg_color)
		
		self.levelRect = self.levelImage.get_rect()
		self.levelRect.right = self.scoreRect.right
		self.levelRect.top = self.scoreRect.bottom + 10