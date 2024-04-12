import pygame, sys, random, time, button

pygame.init()

display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

screen = pygame.display.set_mode((screen_width-100,screen_height-100),pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption('LASTLETTER')

button1 = button.Button(300, 250, 200, 100, (0,255,25), "Click Me!")

while True:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Game = False
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if button1.is_clicked(event.pos):
				print("Button Clicked!")
	button1.draw(screen)
	
	pygame.display.update()
	clock.tick(60)