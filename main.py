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

font = pygame.font.Font("assets/dfont/iFlash 502 Regular.ttf", 32)

checkBoxImgChecked = "assets/img/checke_box.png"
checkBoxImg = "assets/img/checke_box_empty.png"

play = Button(10, 25,width=425,height=45)
option = Button(441, 25,width=400,height=45)
credit = Button(842, 25,width=420,height=45)

removePlayer = Button(80, 160,width=21,height=33,image_path="assets/img/Arrow_l.png")
addPlayer = Button(350, 160,width=21,height=33,image_path="assets/img/Arrow_r.png")

playerCount = 2
playerCountText = font.render(f"{playerCount} Players", True, (255, 255, 255))


gameMode = 1
gameModeEasy = Button(80, 237,width=55,height=56,image_path="assets/img/checke_box.png")
gameModeMedium = Button(80, 340,width=55,height=56,image_path="assets/img/checke_box_empty.png")
gameModeHard = Button(80, 443,width=55,height=56,image_path="assets/img/checke_box_empty.png")



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

			#buttons to handle number of players
			if addPlayer.is_clicked(event.pos):
				playerCount = (playerCount + 1) if playerCount!=4 else 2

			elif removePlayer.is_clicked(event.pos):
				playerCount = (playerCount - 1) if playerCount!=2 else 4

			#buttons to handle game mode
			if gameModeEasy.is_clicked(event.pos):
				gameMode = 1
			elif gameModeMedium.is_clicked(event.pos):
				gameMode = 2
			elif gameModeHard.is_clicked(event.pos):
				gameMode = 3
		##handle player name input
		for index, player in enumerate(players):
			player.active = True if index < playerCount else False
			player.handle_input(event)


	##draw only if the user in the play section
	if background.image_path.find("play")!=-1:
		for player in players:
			player.draw(screen)
	
		###draw buttons
		addPlayer.draw(screen)
		removePlayer.draw(screen)

		gameModeEasy.draw(screen)
		gameModeMedium.draw(screen)
		gameModeHard.draw(screen)

		gameModeEasy.image_path = checkBoxImgChecked if gameMode==1 else checkBoxImg
		gameModeMedium.image_path = checkBoxImgChecked if gameMode==2 else checkBoxImg
		gameModeHard.image_path = checkBoxImgChecked if gameMode==3 else checkBoxImg

		###draw text
		playerCountText = font.render(f"{playerCount} Players", True, (255, 255, 255))
		screen.blit(playerCountText, (150,160))

		screen.blit(font.render("Easy", True, (255, 255, 255)), (150,250))
		screen.blit(font.render("Medium", True, (255, 255, 255)), (150,350))
		screen.blit(font.render("Hard", True, (255, 255, 255)), (150,450))



	pygame.display.update()
	clock.tick(60)