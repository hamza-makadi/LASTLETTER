import pygame, sys, random, time

pygame.init()

display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

screen = pygame.display.set_mode((screen_width-100,screen_height-100),pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption('LASTLETTER')

while True:
	screen.fill((255, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Game = False
			pygame.quit()
			sys.exit()
	pygame.display.update()
	clock.tick(60)