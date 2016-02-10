#! python3
# alien_invasion


import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from gameStats import GameStats
import game_functions as gf
from buttons import Button
from scoreboard import Scoreboard


def run_game():
	#Initializes the settings needed for pygame to run properly
	pygame.init()
	
	aiSettings = Settings()
	#Display mode called 'screen' is made, with 1200 x 800 dimensions
	#Screen is where the game elements are shown
	screen = pygame.display.set_mode(
		(aiSettings.screen_width,aiSettings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#Sets background colour
	
	stats = GameStats(aiSettings)
	sb = Scoreboard(aiSettings, screen, stats)
	
	
	#Makes a ship on screen
	ship = Ship(aiSettings,screen)
	#Bullets! - make a group called bullets
	bullets = Group()
	#Aliens are made
	aliens = Group()
	
	#Calls on the createFleet function
	gf.createFleet(aiSettings, screen, ship, aliens)
	
	playButton = Button(aiSettings, screen, "Click to Play")
	
	while True:
		gf.check_events(aiSettings, screen, stats, sb, playButton, ship, aliens, bullets)
		sb.showScore()
		if stats.game_active:
			ship.update()
			gf.updateBullets(aiSettings, screen, stats, sb, ship, aliens, bullets)
			gf.updateAliens(aiSettings, stats, screen, ship, aliens, bullets)
	
		gf.update_screen(aiSettings, screen, stats, sb, ship, aliens, bullets, playButton)
	


		
run_game()