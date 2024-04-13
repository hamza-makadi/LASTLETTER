import pygame, sys, random, time
from background import BackgroundImage
from button import Button
from player import Player 

pygame.init()

display_info = pygame.display.Info()
screen_width = display_info.current_w-100
screen_height = display_info.current_h-100

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption('LASTLETTER')


play = Button(10, 25,width=425,height=45)
option = Button(441, 25,width=400,height=45)
credit = Button(842, 25,width=420,height=45)

background = BackgroundImage(screen,"assets/img/play_menu.png",screen_width,screen_height)

players = [Player(550,100,True),Player(950,100,True),Player(550,300,False),Player(950,300,False)]

while True:
	##display background image
	background.display()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		elif event.type == pygame.MOUSEBUTTONDOWN:

			##handle player image changes
			for player in players:
				player.change_player_image(event)

			#handle game menu buttons (play / option / credit)
			if play.is_clicked(event.pos):
				background = BackgroundImage(screen,"assets/img/play_menu.png",screen_width,screen_height)
			elif option.is_clicked(event.pos):
				background = BackgroundImage(screen,"assets/img/option_menu.png",screen_width,screen_height)
			elif credit.is_clicked(event.pos):
				background = BackgroundImage(screen,"assets/img/credit_menu.png",screen_width,screen_height)
				
		##handle player name input
		for player in players:
			player.handle_input(event)
	

	##draw players images if the user in the play section
	if background.image_path.find("play")!=-1:
		for player in players:
			player.draw(screen)
	
	
	pygame.display.update()
	clock.tick(60)