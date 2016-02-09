#Isolates event loop

import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def checkKeyDownEvents(event, aiSettings, screen, stats, playButton, ship, aliens, bullets):
#Respond to keypresses and mouse events
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(aiSettings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_p:
		startGame(aiSettings, stats, screen, ship, aliens, bullets)
		
def checkKeyUpEvents(event,ship):
	#When the key is not held down
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False
	if event.key == pygame.K_UP:
		ship.moving_up = False
	if event.key == pygame.K_DOWN:
		ship.moving_down = False
		
def check_events(aiSettings, screen, stats, playButton, ship, aliens, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			checkKeyDownEvents(event, aiSettings, screen, stats, playButton, ship, aliens, bullets)
		elif event.type == pygame.KEYUP:
			checkKeyUpEvents(event,ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			checkPlayButton(aiSettings, screen, stats, playButton, ship, aliens, bullets, mouse_x, mouse_y)
		
def startGame(aiSettings, stats, screen, ship, aliens, bullets):
	stats.resetStats()
	stats.game_active = True
		
	#Erase the whole game screen
	aliens.empty()
	bullets.empty()
	
	#Restart game
	createFleet(aiSettings, screen, ship, aliens)
	ship.centerShip()
		
	pygame.mouse.set_visible(False)
	
def checkPlayButton(aiSettings, screen, stats, playButton, ship, aliens, bullets, mouse_x, mouse_y):
	buttonClicked = playButton.rect.collidepoint(mouse_x,mouse_y)
	if buttonClicked and not stats.game_active:	
		startGame(aiSettings, stats, screen, ship, aliens, bullets)
		
def update_screen(aiSettings, screen, stats, ship, aliens, bullets, playButton):
	#Redraws screen

	screen.fill(aiSettings.bg_color)	
	for bullet in bullets.sprites():
		bullet.drawBullet()
	ship.blitme()
	aliens.draw(screen)
	
	#Order matters & prints this after everyhing else
	if not stats.game_active:
		playButton.drawButton() 
	
	#Updates the gamescreen
	pygame.display.flip()
	
	
def fire_bullet(aiSettings,screen,ship,bullets):
	if len(bullets) < aiSettings.bulletsAllowed:
		newBullet = Bullet(aiSettings,screen,ship)
		bullets.add(newBullet)
		
		
def updateBullets(aiSettings, screen, ship, aliens, bullets):
	bullets.update()
#Use a copy function since it is not good idea to take things from a loop
	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)
	
	checkCollision(aiSettings, screen, ship, aliens, bullets)
	
def checkCollision(aiSettings, screen, ship, aliens, bullets):
	#Checks for collision then gets rid of both bullet and alien if hit
	collisions = pygame.sprite.groupcollide(bullets,aliens,True, True)
	#If there are no more aliens, creates another fleet
	if len(aliens) == 0 :
		bullets.empty()
		createFleet(aiSettings,screen, ship, aliens)

			
def geNumberAliensX(aiSettings, alienWidth):
	#  number of aliens in a row
	availableSpaceX = aiSettings.screen_width - 2* alienWidth
	numberAliensX = int(availableSpaceX / (2*alienWidth))
	return numberAliensX

	
def createAlien(aiSettings, screen, aliens, alienNumber, rowNumber):
		alien = Alien(aiSettings, screen)
		alienWidth = alien.rect.width
		alien.x = alienWidth + 2 * alienWidth * alienNumber
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowNumber
		aliens.add(alien)
	
def createFleet(aiSettings, screen, ship, aliens):
	#Create alien and find number of aliens in a row
	alien = Alien(aiSettings, screen)
	numberAliensX = geNumberAliensX(aiSettings, alien.rect.width)
	numberRows = getNumberRows(aiSettings, ship.rect.height, alien.rect.height)

	#Printing out aliens to form a fleet
	for rowNumber in range(numberRows):
		for alienNumber in range(numberAliensX):
			createAlien(aiSettings, screen, aliens, alienNumber, rowNumber)

def updateAliens(aiSettings, stats, screen, ship, aliens, bullets):
	"""Updates position of all aliens"""
	checkFleetEdges(aiSettings, aliens)
	aliens.update() #Moves aliens 1 pixel to the right
	
	if pygame.sprite.spritecollideany(ship, aliens):
		shipHit(aiSettings, stats, screen, ship, aliens, bullets)
	
	checkAliensBottom(aiSettings, stats, screen, ship, aliens, bullets)
		
def getNumberRows(aiSettings,shipHeight, alienHeight):
	"""Determine number of rows aliens that fit on the screen"""
	availableSpaceY = (aiSettings.screen_height - (3 * alienHeight) - shipHeight)
	numberRows = int(availableSpaceY / (2 * alienHeight))
	return numberRows

def checkFleetEdges(aiSettings, aliens):
	for alien in aliens.sprites():
		if alien.checkEdges():
			changeFleetDirection(aiSettings, aliens)
			break
			
def changeFleetDirection(aiSettings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += aiSettings.fleetDropSpeed
	aiSettings.fleetDirection *= -1
	
def shipHit(aiSettings, stats, screen, ship, aliens, bullets):
	"""Respond to hit by alien"""
	if stats.shipsLeft > 0 :
		stats.shipsLeft -=1 #Decrement 'life'
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)
	#Clears screen
	aliens.empty()
	bullets.empty()
	
	#Create new fleet and ship
	createFleet(aiSettings, screen, ship, aliens)
	ship.centerShip()
	
	#Pause
	sleep(0.5)

	
	
def checkAliensBottom(aiSettings, stats, screen, ship, aliens, bullets):
	"""did aliens win?"""
	screenRect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screenRect.bottom:
			shipHit(aiSettings, stats, screen, ship, aliens, bullets)
			break
