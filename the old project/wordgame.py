import pygame,sys,threading
from pygame import mixer
from pygame.locals import *
from random import *
import random
from time import *

pygame.init()
screen = pygame.display.set_mode((1500,800))#pygame.NOFRAME)
clock = pygame.time.Clock()
pygame.display.set_caption('LASTLET')

#######

font = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',25)

#######

mixer.music.load('.\data\music\piano1.mp3')
mixer.music.play(-1)
click = mixer.Sound('.\data\music\click.wav')

######

play_menu=pygame.image.load('.\data\img\play_menu.png')
option_menu=pygame.image.load('.\data\img\option_menu.png')
credit_menu=pygame.image.load('.\data\img\credit_menu.png')
left=pygame.image.load('.\data\img\Arrow_l.png')
right=pygame.image.load('.\data\img\Arrow_r.png')
m_button=pygame.image.load('.\data\img\Medium_button.png')
m_button_pressed=pygame.image.load('.\data\img\Medium_button_pressed.png')
icon_2=pygame.image.load('.\data\img\Icons2.png')
check_box=pygame.image.load('.\data\img\checke_box.png')
check_box_empty=pygame.image.load('.\data\img\checke_box_empty.png')
empty=pygame.image.load('.\data\img\Empty1.png')
loading=pygame.image.load('.\data\img\loading.png')
playing1=pygame.image.load('.\data\img\Playing\Player1.png')
playing2=pygame.image.load('.\data\img\Playing\Player2.png')
playing3=pygame.image.load('.\data\img\Playing\Player3.png')
playing4=pygame.image.load('.\data\img\Playing\Player4.png')
playing1_2=pygame.image.load('.\data\img\Playing\Player2_1.png')
playing2_2=pygame.image.load('.\data\img\Playing\Player2_2.png')

#faces#######

face=[pygame.image.load('.\data\img\icons\Face1.png'),
		pygame.image.load('.\data\img\icons\Face2.png'),
		pygame.image.load('.\data\img\icons\Face3.png'),
		pygame.image.load('.\data\img\icons\Face4.png'),
		pygame.image.load('.\data\img\icons\Face5.png'),
		pygame.image.load('.\data\img\icons\Face6.png'),
		pygame.image.load('.\data\img\icons\Face7.png'),
		pygame.image.load('.\data\img\icons\Face8.png')
		]

four_player=[
		pygame.image.load('.\data\img\Playing\easy\_0.png'),
		pygame.image.load('.\data\img\Playing\easy\_1.png'),
		pygame.image.load('.\data\img\Playing\easy\_2.png'),
		pygame.image.load('.\data\img\Playing\easy\_3.png'),
		pygame.image.load('.\data\img\Playing\easy\_4.png'),
		pygame.image.load('.\data\img\Playing\easy\_5.png'),
		pygame.image.load('.\data\img\Playing\easy\_6.png'),
		pygame.image.load('.\data\img\Playing\easy\_7.png'),
		pygame.image.load('.\data\img\Playing\easy\_8.png'),
		pygame.image.load('.\data\img\Playing\easy\_9.png'),
		pygame.image.load('.\data\img\Playing\easy\_10.png'),
		pygame.image.load('.\data\img\Playing\easy\_11.png'),
		pygame.image.load('.\data\img\Playing\easy\_12.png'),
		pygame.image.load('.\data\img\Playing\easy\_13.png'),
		pygame.image.load('.\data\img\Playing\easy\_14.png'),
		pygame.image.load('.\data\img\Playing\easy\_15.png'),
		pygame.image.load('.\data\img\Playing\easy\_16.png'),
		pygame.image.load('.\data\img\Playing\easy\_17.png'),
		pygame.image.load('.\data\img\Playing\easy\_18.png'),
		pygame.image.load('.\data\img\Playing\easy\_19.png'),
		pygame.image.load('.\data\img\Playing\easy\_20.png'),
		]

three_player=[
		pygame.image.load('.\data\img\Playing\easy\_3_0.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_1.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_2.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_3.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_4.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_5.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_6.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_7.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_8.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_9.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_10.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_11.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_12.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_13.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_14.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_15.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_16.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_17.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_18.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_19.png'),
		pygame.image.load('.\data\img\Playing\easy\_3_20.png'),
		]

two_player=[
		pygame.image.load('.\data\img\Playing\easy\_2_0.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_1.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_2.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_3.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_4.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_5.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_6.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_7.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_8.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_9.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_10.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_11.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_12.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_13.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_14.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_15.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_16.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_17.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_18.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_19.png'),
		pygame.image.load('.\data\img\Playing\easy\_2_20.png'),
		]

four_player_m=[
		pygame.image.load('.\data\img\Playing\medium\_10.png'),
		pygame.image.load('.\data\img\Playing\medium\_9.png'),
		pygame.image.load('.\data\img\Playing\medium\_8.png'),
		pygame.image.load('.\data\img\Playing\medium\_7.png'),
		pygame.image.load('.\data\img\Playing\medium\_6.png'),
		pygame.image.load('.\data\img\Playing\medium\_5.png'),
		pygame.image.load('.\data\img\Playing\medium\_4.png'),
		pygame.image.load('.\data\img\Playing\medium\_3.png'),
		pygame.image.load('.\data\img\Playing\medium\_2.png'),
		pygame.image.load('.\data\img\Playing\medium\_1.png'),
		pygame.image.load('.\data\img\Playing\medium\_0.png')
		]

three_player_m=[
		pygame.image.load('.\data\img\Playing\medium\_3_10.png'),
		pygame.image.load('.\data\img\Playing\medium\_3_9.png'),
		pygame.image.load('.\data\img\Playing\medium\_3_8.png'),
		pygame.image.load('.\data\img\Playing\medium\_3_7.png'),
		pygame.image.load('.\data\img\Playing\medium\_3_6.png'),
		pygame.image.load('.\data\img\Playing\medium\_3_5.png'),
		pygame.image.load('.\data\img\Playing\medium\_3_4.png'),
		pygame.image.load('.\data\img\Playing\medium\_3_3.png'),
		pygame.image.load('.\data\img\Playing\medium\_3_2.png'),
		pygame.image.load('.\data\img\Playing\medium\_3_1.png'),
		pygame.image.load('.\data\img\Playing\medium\_3_0.png')
		]

two_player_m=[
		pygame.image.load('.\data\img\Playing\medium\_2_10.png'),
		pygame.image.load('.\data\img\Playing\medium\_2_9.png'),
		pygame.image.load('.\data\img\Playing\medium\_2_8.png'),
		pygame.image.load('.\data\img\Playing\medium\_2_7.png'),
		pygame.image.load('.\data\img\Playing\medium\_2_6.png'),
		pygame.image.load('.\data\img\Playing\medium\_2_5.png'),
		pygame.image.load('.\data\img\Playing\medium\_2_4.png'),
		pygame.image.load('.\data\img\Playing\medium\_2_3.png'),
		pygame.image.load('.\data\img\Playing\medium\_2_2.png'),
		pygame.image.load('.\data\img\Playing\medium\_2_1.png'),
		pygame.image.load('.\data\img\Playing\medium\_2_0.png')
		]

four_player_h=[
		pygame.image.load('.\data\img\Playing\hard\_5.png'),
		pygame.image.load('.\data\img\Playing\hard\_4.png'),
		pygame.image.load('.\data\img\Playing\hard\_3.png'),
		pygame.image.load('.\data\img\Playing\hard\_2.png'),
		pygame.image.load('.\data\img\Playing\hard\_1.png'),
		pygame.image.load('.\data\img\Playing\hard\_0.png')
		]

three_player_h=[
		pygame.image.load('.\data\img\Playing\hard\_3_5.png'),
		pygame.image.load('.\data\img\Playing\hard\_3_4.png'),
		pygame.image.load('.\data\img\Playing\hard\_3_3.png'),
		pygame.image.load('.\data\img\Playing\hard\_3_2.png'),
		pygame.image.load('.\data\img\Playing\hard\_3_1.png'),
		pygame.image.load('.\data\img\Playing\hard\_3_0.png')
		]

two_player_h=[
		pygame.image.load('.\data\img\Playing\hard\_2_5.png'),
		pygame.image.load('.\data\img\Playing\hard\_2_4.png'),
		pygame.image.load('.\data\img\Playing\hard\_2_3.png'),
		pygame.image.load('.\data\img\Playing\hard\_2_2.png'),
		pygame.image.load('.\data\img\Playing\hard\_2_1.png'),
		pygame.image.load('.\data\img\Playing\hard\_2_0.png')
		]

########

letter =chr(randint(97,120))
user_text = letter

##color##

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,0,255)
darkgray = (15, 15, 15)
black = (0, 0, 0)
gray = (25, 25, 25)
rect_color_active=(171,216,209)
rect_color_passive=(102,130,126)

############

x=0
y=[0,0,0,0]
Game=True
clicked = False
winner1=False
winner2=False
winner3=False
winner4=False
music = True
sound_check=True
active = [False,False,False,False]
game = [True,False,False,False]
Menu = [True,False,False]
players = [True,False,False]
difficulty =[True,False,False]
player_name=['','','','']
player_img=[[True,False,False,False,False,False,False,False],
			[True,False,False,False,False,False,False,False],
			[True,False,False,False,False,False,False,False],
			[True,False,False,False,False,False,False,False]
		   ]
winner_4 =[1,0,0,0]
winner_3=[1,0,0]
winner_2=[1,0]
color=[rect_color_passive,rect_color_passive,rect_color_passive,rect_color_passive]

##class for button ##

class button():
    ##colours for button
    text_col = (0, 0, 0)
    white = (255, 255, 255)
    def __init__(self, x, y, text,w ,h,font):
        self.x = x
        self.y = y
        self.text = text
        self.w = w
        self.h = h
        self.font = font
    def draw_button(self):
        global clicked
        action = False
        ######get mouse position
        pos = pygame.mouse.get_pos()
        #######create pygame Rect object for the button
        button_rect = Rect(self.x-5, self.y, self.w, self.h)
        #pygame.draw.rect(screen,white,button_rect,1)
        #######add text to button
        text_img = self.font.render(self.text, True, self.white)
        screen.blit(text_img, (self.x , self.y))
        #######check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            text_img = self.font.render(self.text, True, gray)
            screen.blit(text_img, (self.x , self.y))
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                text_img = self.font.render(self.text, True, black)
                screen.blit(text_img, (self.x , self.y))
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            return action

def countdown():
	global my_timer,my_timer1,my_timer2,my_timer3
	while True:
		my_timer = 5
		my_timer2=10
		my_timer1= 20
		my_timer3= 5
		while game[1] and my_timer>0 :
			my_timer = my_timer - 1
			sleep(1)
			if my_timer==0:
				my_timer=5
			if Game==False:
				break
		while game[2] and my_timer>0 and difficulty[2]:
			my_timer3 = my_timer3 -1
			sleep(1)
			if Game==False:
				break
		while game[2] and my_timer1>0 and difficulty[0]:
			my_timer1 = my_timer1 -1
			sleep(1)
			if Game==False:
				break
		while game[2] and my_timer2>0 and difficulty[1] :
			my_timer2 = my_timer2 -1
			sleep(1)
			if Game==False:
				break
		if Game==False:
			break


countdown_thread = threading.Thread(target = countdown)
countdown_thread.start()

with open("words.txt", "r") as f:	
	t = []
	for line in f:
		line = line.replace('\n','')
		line = line.replace('_',' ')
		t.append(line)

play = button(10,35,'',510,45,font)
option = button(525,35,'',470,45,font)
credit = button(1000,35,'',500,45,font)

next_R=button(400,195,'',30,30,font)
next_L=button(122,195,'',30,30,font)

next_img1_L=button(628,160,'',30,30,font)
next_img1_R=button(800,160,'',30,30,font)

next_img2_L=button(1128,160,'',30,30,font)
next_img2_R=button(1300,160,'',30,30,font)

next_img3_L=button(628,460,'',30,30,font)
next_img3_R=button(800,460,'',30,30,font)

next_img4_L=button(1128,460,'',30,30,font)
next_img4_R=button(1300,460,'',30,30,font)

easy=button(102,320,'',58,58,font)
medium=button(102,470,'',58,58,font)
hard=button(102,620,'',58,58,font)

play_button=button(900,650,'',450,95,font)
help_button = button(780,650,'',100,95,font)

music_on = button(1120,230,'',58,58,font)
music_off = button(720,230,'',58,58,font)

sound_on = button(1120,430,'',58,58,font)
sound_off = button(720,430,'',58,58,font)

play_again = button(780,550,'',450,100,font)
main_menu = button(270,550,'',450,100,font)

input_rect1=pygame.Rect(642,250,170,40)
input_rect2=pygame.Rect(1142,250,170,40)
input_rect3=pygame.Rect(642,550,170,40)
input_rect4=pygame.Rect(1142,550,170,40)

input_rect5=pygame.Rect(420,210,800,80)
input_rect6=pygame.Rect(420,600,800,80)
input_rect7=pygame.Rect(50,650,600,60)
input_rect8=pygame.Rect(760,650,600,60)
input_rect9=pygame.Rect(50,250,600,60)
input_rect10=pygame.Rect(760,250,600,60)

while Game:
	while game[0]:
		while Menu[0]:
			screen.blit(play_menu,(0,0))
			screen.blit(right,(400,195))
			screen.blit(left,(122,195))
			screen.blit(pygame.transform.scale(m_button, (450, 95)),(900,650))
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAY  >',True,
				(255,255,255)),(1040,661))
			if players[0]:
				player_name=[player_name[0],player_name[1],'','']
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('2 PLAYERS',True,
				(255,255,255)),(200,193))
				
				screen.blit(empty,(650,400))
				screen.blit(empty,(1150,400))

				screen.blit(right,(800,160))
				screen.blit(left,(628,160))

				screen.blit(right,(1300,160))
				screen.blit(left,(1128,160))

				screen.blit(right,(800,460))
				screen.blit(left,(628,460))

				screen.blit(right,(1300,460))
				screen.blit(left,(1128,460))

				for i in range(8):
					if player_img[0][i]==True:
						screen.blit(face[i],(650,100))
					if player_img[1][i]==True:
						screen.blit(face[i],(1150,100))
				pygame.draw.rect(screen,color[0],input_rect1,3)
				text_surface1 = font.render(player_name[0],True,(255,255,255))
				screen.blit(text_surface1,(input_rect1.x+11,input_rect1.y+5))
				input_rect1.w = max(170,text_surface1.get_width()+20)

				pygame.draw.rect(screen,color[1],input_rect2,3)
				text_surface2 = font.render(player_name[1],True,(255,255,255))
				screen.blit(text_surface2,(input_rect2.x+11,input_rect2.y+5))
				input_rect2.w = max(170,text_surface2.get_width()+20)

				pygame.draw.rect(screen,color[2],input_rect3,3)
				text_surface3 = font.render(player_name[2],True,(255,255,255))
				screen.blit(text_surface3,(input_rect3.x+11,input_rect3.y+5))
				input_rect3.w = max(170,text_surface3.get_width()+20)
				
				pygame.draw.rect(screen,color[3],input_rect4,3)
				text_surface4 = font.render(player_name[3],True,(255,255,255))
				screen.blit(text_surface4,(input_rect4.x+11,input_rect4.y+5))
				input_rect4.w = max(170,text_surface4.get_width()+20)

			if players[1]:
				player_name=[player_name[0],player_name[1],player_name[2],'']
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('3 PLAYERS',True,
				(255,255,255)),(200,193))
				screen.blit(empty,(1150,400))

				screen.blit(right,(800,160))
				screen.blit(left,(628,160))

				screen.blit(right,(1300,160))
				screen.blit(left,(1128,160))

				screen.blit(right,(1300,460))
				screen.blit(left,(1128,460))

				screen.blit(right,(800,460))
				screen.blit(left,(628,460))

				for i in range(8):
					if player_img[0][i]==True:
						screen.blit(face[i],(650,100))
					if player_img[1][i]==True:
						screen.blit(face[i],(1150,100))
					if player_img[2][i]==True:
						screen.blit(face[i],(650,400))
				pygame.draw.rect(screen,color[0],input_rect1,3)
				text_surface1 = font.render(player_name[0],True,(255,255,255))
				screen.blit(text_surface1,(input_rect1.x+11,input_rect1.y+5))
				input_rect1.w = max(170,text_surface1.get_width()+20)

				pygame.draw.rect(screen,color[1],input_rect2,3)
				text_surface2 = font.render(player_name[1],True,(255,255,255))
				screen.blit(text_surface2,(input_rect2.x+11,input_rect2.y+5))
				input_rect2.w = max(170,text_surface2.get_width()+20)

				pygame.draw.rect(screen,color[2],input_rect3,3)
				text_surface3 = font.render(player_name[2],True,(255,255,255))
				screen.blit(text_surface3,(input_rect3.x+11,input_rect3.y+5))
				input_rect3.w = max(170,text_surface3.get_width()+20)
				
				pygame.draw.rect(screen,color[3],input_rect4,3)
				text_surface4 = font.render(player_name[3],True,(255,255,255))
				screen.blit(text_surface4,(input_rect4.x+11,input_rect4.y+5))
				input_rect4.w = max(170,text_surface4.get_width()+20)
			if players[2]:
				player_name=[player_name[0],player_name[1],player_name[2],player_name[3]]
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('4 PLAYERS',True,
				(255,255,255)),(200,193))

				screen.blit(right,(800,160))
				screen.blit(left,(628,160))

				screen.blit(right,(1300,160))
				screen.blit(left,(1128,160))

				screen.blit(right,(1300,460))
				screen.blit(left,(1128,460))

				screen.blit(right,(800,460))
				screen.blit(left,(628,460))


				for i in range(8):
					if player_img[0][i]==True:
						screen.blit(face[i],(650,100))
					if player_img[1][i]==True:
						screen.blit(face[i],(1150,100))
					if player_img[2][i]==True:
						screen.blit(face[i],(650,400))
					if player_img[3][i]==True:
						screen.blit(face[i],(1150,400))

				pygame.draw.rect(screen,color[0],input_rect1,3)
				text_surface1 = font.render(player_name[0],True,(255,255,255))
				screen.blit(text_surface1,(input_rect1.x+11,input_rect1.y+5))
				input_rect1.w = max(170,text_surface1.get_width()+20)

				pygame.draw.rect(screen,color[1],input_rect2,3)
				text_surface2 = font.render(player_name[1],True,(255,255,255))
				screen.blit(text_surface2,(input_rect2.x+11,input_rect2.y+5))
				input_rect2.w = max(170,text_surface2.get_width()+20)

				pygame.draw.rect(screen,color[2],input_rect3,3)
				text_surface3 = font.render(player_name[2],True,(255,255,255))
				screen.blit(text_surface3,(input_rect3.x+11,input_rect3.y+5))
				input_rect3.w = max(170,text_surface3.get_width()+20)

				pygame.draw.rect(screen,color[3],input_rect4,3)
				text_surface4 = font.render(player_name[3],True,(255,255,255))
				screen.blit(text_surface4,(input_rect4.x+11,input_rect4.y+5))
				input_rect4.w = max(170,text_surface4.get_width()+20)
			if difficulty[0]:
				screen.blit(check_box,(100,320))
				screen.blit(check_box_empty,(100,470))
				screen.blit(check_box_empty,(100,620))
			if difficulty[1]:
				screen.blit(check_box_empty,(100,320))
				screen.blit(check_box,(100,470))
				screen.blit(check_box_empty,(100,620))
			if difficulty[2]:
				screen.blit(check_box_empty,(100,320))
				screen.blit(check_box_empty,(100,470))
				screen.blit(check_box,(100,620))
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('EASY',True,
				(255,255,255)),(220,322))
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('MEDIUM',True,
				(255,255,255)),(220,472))
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('HARD',True,
				(255,255,255)),(220,622))
			play_button.draw_button()
			easy.draw_button()
			medium.draw_button()
			hard.draw_button()
			next_L.draw_button()
			next_R.draw_button()

			next_img1_L.draw_button()
			next_img1_R.draw_button()

			next_img2_L.draw_button()
			next_img2_R.draw_button()

			next_img3_L.draw_button()
			next_img3_R.draw_button()

			next_img4_L.draw_button()
			next_img4_R.draw_button()
			play.draw_button()
			option.draw_button()
			credit.draw_button()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if play.draw_button() :
					click.play()
					Menu=[True,False,False]
				if option.draw_button() :
					click.play()	
					Menu=[False,True,False]
				if credit.draw_button() :
					click.play()	
					Menu=[False,False,True]
				if Menu[0]:
					if easy.draw_button():
						click.play()
						difficulty=[True,False,False]
					if medium.draw_button():
						click.play()
						difficulty=[False,True,False]
					if hard.draw_button():
						click.play()
						difficulty=[False,False,True]
					if play_button.draw_button():
						click.play()
						screen.blit(pygame.transform.scale(m_button_pressed, (450, 95)),(900,650))
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAY  >',True,
					(255,255,255)),(1040,661))
						timer=3
						game[0]=False
						Menu[0]=False
						game[1]=True
					if next_R.draw_button():
						click.play()
						if players[x]==True :
							if x==2:
								players=[True,False,False]
								x=0
								break
							else:
								players[x]=False
								players[x+1]=True
								x+=1
								break
					if next_L.draw_button():
						click.play()
						if players[x]==True:
							if x==0:
								players=[False,False,True]
								x=2
								break
							else:
								players[x]=False
								players[x-1]=True
								x-=1
								break

					if players[2]:
						if next_img1_R.draw_button():
							click.play()
							if player_img[0][y[0]]==True:
								if y[0]==7:
									player_img[0]=[True,False,False,False,False,False,False,False]
									y[0]=0
									break
								else:
									player_img[0][y[0]]=False
									player_img[0][y[0]+1]=True
									y[0]+=1
									break
						elif next_img1_L.draw_button():
							click.play()
							if player_img[0][y[0]]==True:
								if y[0]==0:
									player_img[0]=[False,False,False,False,False,False,False,True]
									y[0]=7
									break
								else:
									player_img[0][y[0]]=False
									player_img[0][y[0]-1]=True
									y[0]-=1
									break
						elif next_img2_R.draw_button():
							click.play()
							if player_img[1][y[1]]==True:
								if y[1]==7:
									player_img[1]=[True,False,False,False,False,False,False,False]
									y[1]=0
									break
								else:
									player_img[1][y[1]]=False
									player_img[1][y[1]+1]=True
									y[1]+=1
									break
						elif next_img2_L.draw_button():
							click.play()
							if player_img[1][y[1]]==True:
								if y[1]==0:
									player_img[1]=[False,False,False,False,False,False,False,True]
									y[1]=7
									break
								else:
									player_img[1][y[1]]=False
									player_img[1][y[1]-1]=True
									y[1]-=1
									break
						elif next_img3_R.draw_button():
							click.play()
							if player_img[2][y[2]]==True:
								if y[2]==7:
									player_img[2]=[True,False,False,False,False,False,False,False]
									y[2]=0
									break
								else:
									player_img[2][y[2]]=False
									player_img[2][y[2]+1]=True
									y[2]+=1
									break
						elif next_img3_L.draw_button():
							click.play()
							if player_img[2][y[2]]==True:
								if y[2]==0:
									player_img[2]=[False,False,False,False,False,False,False,True]
									y[2]=7
									break
								else:
									player_img[2][y[2]]=False
									player_img[2][y[2]-1]=True
									y[2]-=1
									break
						elif next_img4_R.draw_button():
							click.play()
							if player_img[3][y[3]]==True:
								if y[3]==7:
									player_img[3]=[True,False,False,False,False,False,False,False]
									y[3]=0
									break
								else:
									player_img[3][y[3]]=False
									player_img[3][y[3]+1]=True
									y[3]+=1
									break
						elif next_img4_L.draw_button():
							click.play()
							if player_img[3][y[3]]==True:
								if y[3]==0:
									player_img[3]=[False,False,False,False,False,False,False,True]
									y[3]=7
									break
								else:
									player_img[3][y[3]]=False
									player_img[3][y[3]-1]=True
									y[3]-=1
									break
					elif players[1] :
						if next_img1_R.draw_button():
							click.play()
							if player_img[0][y[0]]==True:
								if y[0]==7:
									player_img[0]=[True,False,False,False,False,False,False,False]
									y[0]=0
									break
								else:
									player_img[0][y[0]]=False
									player_img[0][y[0]+1]=True
									y[0]+=1
									break
						elif next_img1_L.draw_button():
							click.play()
							if player_img[0][y[0]]==True:
								if y[0]==0:
									player_img[0]=[False,False,False,False,False,False,False,True]
									y[0]=7
									break
								else:
									player_img[0][y[0]]=False
									player_img[0][y[0]-1]=True
									y[0]-=1
									break
						elif next_img2_R.draw_button():
							click.play()
							if player_img[1][y[1]]==True:
								if y[1]==7:
									player_img[1]=[True,False,False,False,False,False,False,False]
									y[1]=0
									break
								else:
									player_img[1][y[1]]=False
									player_img[1][y[1]+1]=True
									y[1]+=1
									break
						elif next_img2_L.draw_button():
							click.play()
							if player_img[1][y[1]]==True:
								if y[1]==0:
									player_img[1]=[False,False,False,False,False,False,False,True]
									y[1]=7
									break
								else:
									player_img[1][y[1]]=False
									player_img[1][y[1]-1]=True
									y[1]-=1
									break
						elif next_img3_R.draw_button():
							click.play()
							if player_img[2][y[2]]==True:
								if y[2]==7:
									player_img[2]=[True,False,False,False,False,False,False,False]
									y[2]=0
									break
								else:
									player_img[2][y[2]]=False
									player_img[2][y[2]+1]=True
									y[2]+=1
									break
						elif next_img3_L.draw_button():
							click.play()
							if player_img[2][y[2]]==True:
								if y[2]==0:
									player_img[2]=[False,False,False,False,False,False,False,True]
									y[2]=7
									break
								else:
									player_img[2][y[2]]=False
									player_img[2][y[2]-1]=True
									y[2]-=1
									break
					elif players[0]:
						if next_img1_R.draw_button():
							click.play()
							if player_img[0][y[0]]==True:
								if y[0]==7:
									player_img[0]=[True,False,False,False,False,False,False,False]
									y[0]=0
									break
								else:
									player_img[0][y[0]]=False
									player_img[0][y[0]+1]=True
									y[0]+=1
									break
						elif next_img1_L.draw_button():
							click.play()
							if player_img[0][y[0]]==True:
								if y[0]==0:
									player_img[0]=[False,False,False,False,False,False,False,True]
									y[0]=7
									break
								else:
									player_img[0][y[0]]=False
									player_img[0][y[0]-1]=True
									y[0]-=1
									break
						elif next_img2_R.draw_button():
							click.play()
							if player_img[1][y[1]]==True:
								if y[1]==7:
									player_img[1]=[True,False,False,False,False,False,False,False]
									y[1]=0
									break
								else:
									player_img[1][y[1]]=False
									player_img[1][y[1]+1]=True
									y[1]+=1
									break
						elif next_img2_L.draw_button():
							click.play()
							if player_img[1][y[1]]==True:
								if y[1]==0:
									player_img[1]=[False,False,False,False,False,False,False,True]
									y[1]=7
									break
								else:
									player_img[1][y[1]]=False
									player_img[1][y[1]-1]=True
									y[1]-=1
									break
					

					if event.type ==pygame.MOUSEBUTTONDOWN:
						if input_rect1.collidepoint(event.pos) and active==[False,False,False,False]:
							active[0]=True
						elif input_rect2.collidepoint(event.pos) and active==[False,False,False,False]:
							active[1]=True
						elif input_rect3.collidepoint(event.pos) and players[1] and active==[False,False,False,False]:
							active[2]=True
						elif input_rect3.collidepoint(event.pos) and players[2] and active==[False,False,False,False]:
							active[2]=True
						elif input_rect4.collidepoint(event.pos) and players[2] and active==[False,False,False,False]:
							active[3]=True
						else:
							active=[False,False,False,False]
					if event.type == pygame.KEYDOWN:
						if active[0]:
							if event.key == pygame.K_BACKSPACE :
								player_name[0] = player_name[0][:-1]
							else:
								if len(player_name[0])<9:
									player_name[0] += event.unicode
						elif active[1]:
							if event.key == pygame.K_BACKSPACE :
								player_name[1] = player_name[1][:-1]
							else:
								if len(player_name[1])<9:
									player_name[1] += event.unicode
						elif active[2]:
							if event.key == pygame.K_BACKSPACE :
								player_name[2] = player_name[2][:-1]
							else:
								if len(player_name[2])<9:
									player_name[2] += event.unicode
						elif active[3]:
							if event.key == pygame.K_BACKSPACE :
								player_name[3] = player_name[3][:-1]
							else:
								if len(player_name[3])<9:
									player_name[3] += event.unicode
			if active[0]:
				color[0] = rect_color_active
			elif active[1]:
				color[1] = rect_color_active
			elif active[2]:
				color[2] = rect_color_active
			elif active[3]:
				color[3] = rect_color_active
			else:
				color=[rect_color_passive,rect_color_passive,rect_color_passive,rect_color_passive]
			pygame.display.update()
			clock.tick(240)
		while Menu[1]:
			screen.blit(option_menu,(0,0))
			play.draw_button()
			option.draw_button()
			credit.draw_button()
			music_off.draw_button()
			music_on.draw_button()
			sound_off.draw_button()
			sound_on.draw_button()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if play.draw_button() :
					click.play()
					Menu=[True,False,False]
				if option.draw_button() :
					click.play()	
					Menu=[False,True,False]
				if credit.draw_button() :
					click.play()	
					Menu=[False,False,True]
				if music_on.draw_button():
					click.play()
					mixer.music.unpause()
					music = True
				if music_off.draw_button():
					click.play()
					mixer.music.pause()
					music=False
				if sound_on.draw_button():
					click.play()
					pygame.mixer.Sound.set_volume(click,1.0)
					sound_check = True
				if sound_off.draw_button():
					pygame.mixer.Sound.set_volume(click,0.0)
					sound_check=False
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',80).render('MUSIC :',True,
				(255,255,255)),(220,220))
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render('ON',True,
				(255,255,255)),(1200,220))
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render('OFF',True,
				(255,255,255)),(800,220))
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',80).render('SOUND :',True,
				(255,255,255)),(215,420))
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render('ON',True,
				(255,255,255)),(1200,420))
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render('OFF',True,
				(255,255,255)),(800,420))
			if sound_check:
				screen.blit(check_box_empty,(720,430))
				screen.blit(check_box,(1120,430))
			else:
				screen.blit(check_box,(720,430))
				screen.blit(check_box_empty,(1120,430))
			if music:
				screen.blit(check_box_empty,(720,230))
				screen.blit(check_box,(1120,230))
			else:
				screen.blit(check_box,(720,230))
				screen.blit(check_box_empty,(1120,230))

			pygame.display.update()
			clock.tick(240)
		while Menu[2]:
			screen.blit(credit_menu,(0,0))
			play.draw_button()
			option.draw_button()
			credit.draw_button()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if play.draw_button() :
					click.play()
					Menu=[True,False,False]
				if option.draw_button() :
					click.play()	
					Menu=[False,True,False]
				if credit.draw_button() :	
					click.play()
					Menu=[False,False,True]

			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('HAMZA MAKEDI',True,
						(255,255,255)),(530,250))
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('AYOUB AYARI',True,
						(255,255,255)),(200,540))
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('AYMEN DRIDI',True,
						(255,255,255)),(950,540))
			pygame.display.update()
			clock.tick(240)
		
		pygame.display.update()
		clock.tick(240)
	while game[1]:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		if players[0]:
			screen.blit(loading,(0,0))
			if my_timer != timer :
				timer=my_timer
				if timer < 0:
					timer = 0
			time = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',90).render(str(timer), True, white)
			screen.blit(time, (725, 460))
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',90).render('GET READY !!!',True,
			(255,255,255)),(480,80))
			if len(player_name[0])>0:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(player_name[0],True,
				(255,255,255)),(280,480))
			else:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAYER 1',True,
				(255,255,255)),(280,480))
			if len(player_name[1])>0:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(player_name[1],True,
				(255,255,255)),(980,480))
			else:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAYER 2',True,
				(255,255,255)),(980,480))
			for i in range(8):
				if player_img[0][i]==True:
					screen.blit(pygame.transform.scale(face[i], (300, 300)),(250,200))
				if player_img[1][i]==True:
					screen.blit(pygame.transform.scale(face[i], (300, 300)),(950,200))
		if players[1]:
			screen.blit(loading,(0,0))
			if my_timer != timer :
				timer=my_timer
				if timer < 0:
					timer = 0
			time = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',90).render(str(timer), True, white)
			screen.blit(time, (725, 360))
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',90).render('GET READY !!!',True,
			(255,255,255)),(480,80))
			if len(player_name[0])>0:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(player_name[0],True,
				(255,255,255)),(280,480))
			else:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAYER 1',True,
				(255,255,255)),(280,480))
			if len(player_name[1])>0:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(player_name[1],True,
				(255,255,255)),(980,480))
			else:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAYER 2',True,
				(255,255,255)),(980,480))
			if len(player_name[0])>0:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(player_name[2],True,
				(255,255,255)),(635,720))
			else:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAYER 3',True,
				(255,255,255)),(635,720))
			for i in range(8):
				if player_img[0][i]==True:
					screen.blit(pygame.transform.scale(face[i], (300, 300)),(250,200))
				if player_img[1][i]==True:
					screen.blit(pygame.transform.scale(face[i], (300, 300)),(950,200))
				if player_img[2][i]==True:
					screen.blit(pygame.transform.scale(face[i], (300, 300)),(605,450))
		if players[2]:
			screen.blit(loading,(0,0))
			if my_timer != timer :
				timer=my_timer
				if timer < 0:
					timer = 0
			time = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',90).render(str(timer), True, white)
			screen.blit(time, (725, 360))
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',90).render('GET READY !!!',True,
			(255,255,255)),(480,80))
			if len(player_name[0])>0:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',40).render(player_name[0],True,
				(255,255,255)),(268,395))
			else:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',40).render('PLAYER 1',True,
				(255,255,255)),(268,395))
			if len(player_name[1])>0:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',40).render(player_name[1],True,
				(255,255,255)),(268,395))
			else:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',40).render('PLAYER 2',True,
				(255,255,255)),(1069,395))
			if len(player_name[0])>0:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',40).render(player_name[2],True,
				(255,255,255)),(268,649))
			else:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',40).render('PLAYER 3',True,
				(255,255,255)),(268,649))
			if len(player_name[0])>0:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',40).render(player_name[3],True,
				(255,255,255)),(1069,649))
			else:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',40).render('PLAYER 4',True,
				(255,255,255)),(1069,649))
			for i in range(8):
				if player_img[0][i]==True:
					screen.blit(pygame.transform.scale(face[i], (200, 200)),(250,200))
				if player_img[1][i]==True:
					screen.blit(pygame.transform.scale(face[i], (200, 200)),(1050,200))
				if player_img[2][i]==True:
					screen.blit(pygame.transform.scale(face[i], (200, 200)),(250,450))
				if player_img[3][i]==True:
					screen.blit(pygame.transform.scale(face[i], (200, 200)),(1050,450))
		if timer==0:
			game[1]=False
			game[2]=True
		pygame.display.update()
		clock.tick(240)
	while game[2]:
		while players[0] and difficulty[0]:
			if my_timer1 != timer :
				timer=my_timer1
				if timer < 0:
					timer = 0
			time = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(str(timer).zfill(2), True, white)
			screen.blit(two_player[timer],(0,0))
			screen.blit(time, (717, 351))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE and len(user_text)>1:
						user_text = user_text[:-1]
					if event.key == pygame.K_BACKSPACE:
						pass
					elif event.key == pygame.K_RETURN:
						for i in range(144556):
							if t[i]==user_text:
								my_timer = 20
								if winner_2==[1,0]:
									letter = user_text[-1]
									user_text = letter
									winner_2=[0,1]
									my_timer1=20
								else:
									letter = user_text[-1]
									user_text = letter
									winner_2=[1,0]
									my_timer1=20
					else:
						if len(user_text)<20:
							user_text += event.unicode
			if timer!=0 :
				if winner_2==[1,0]:
					screen.blit(playing1_2,(0,0))
					pygame.draw.rect(screen,color[1],input_rect5,3)
					text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(user_text,True,
						(255,255,255))
					screen.blit(text_surface,(input_rect5.x+11,input_rect5.y+5))
					last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(letter,
					 True, (255,255,255))
					screen.blit(last_letter, (1160, 115))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('word start with letter :',True,
						(255,255,255)),(420,110))
					if len(player_name[0])>0:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(player_name[0],True,
						(255,255,255)),(420,35))
					else:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAYER 1',True,
						(255,255,255)),(420,35))
					for i in range(8):
						if player_img[0][i]==True:
							screen.blit(pygame.transform.scale(face[i],(400,400)),(0,-5))
				else:
					screen.blit(playing2_2,(0,0))
					pygame.draw.rect(screen,color[1],input_rect6,3)
					text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(user_text,True,
						(255,255,255))
					screen.blit(text_surface,(input_rect6.x+11,input_rect6.y+5))
					last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(letter,
					 True, (255,255,255))
					screen.blit(last_letter, (1160, 495))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('word start with letter :',True,
						(255,255,255)),(420,490))
					if len(player_name[1])>0:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(player_name[1],True,
						(255,255,255)),(420,420))
					else:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAYER 2',True,
						(255,255,255)),(420,420))
					for i in range(8):
						if player_img[1][i]==True:
							screen.blit(pygame.transform.scale(face[i],(400,400)),(0,370))
						
			else:
				if winner_2==[1,0]:
					winner2=True
					break
				else:
					winner1=True
					break
			pygame.display.update()
			clock.tick(240)
		while players[0] and difficulty[1]:
			if my_timer2 != timer :
				timer=my_timer2
				if timer < 0:
					timer = 0
			time = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(str(timer).zfill(2), True, white)
			screen.blit(two_player_m[timer],(0,0))
			screen.blit(time, (717, 351))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE and len(user_text)>1:
						user_text = user_text[:-1]
					if event.key == pygame.K_BACKSPACE:
						pass
					elif event.key == pygame.K_RETURN:
						for i in range(144556):
							if t[i]==user_text:
								my_timer2 = 10
								if winner_2==[1,0]:
									letter = user_text[-1]
									user_text = letter
									winner_2=[0,1]
									my_timer2=10
								else:
									letter = user_text[-1]
									user_text = letter
									winner_2=[1,0]
									my_timer2=10
					else:
						if len(user_text)<20:
							user_text += event.unicode

			if timer!=0 :
				if winner_2==[1,0]:
					screen.blit(playing1_2,(0,0))
					pygame.draw.rect(screen,color[1],input_rect5,3)
					text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(user_text,True,
						(255,255,255))
					screen.blit(text_surface,(input_rect5.x+11,input_rect5.y+5))
					last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(letter,
					 True, (255,255,255))
					screen.blit(last_letter, (1160, 115))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('word start with letter :',True,
						(255,255,255)),(420,110))
					if len(player_name[0])>0:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(player_name[0],True,
						(255,255,255)),(420,35))
					else:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAYER 1',True,
						(255,255,255)),(420,35))
					for i in range(8):
						if player_img[0][i]==True:
							screen.blit(pygame.transform.scale(face[i],(400,400)),(0,-5))
				else:
					screen.blit(playing2_2,(0,0))
					pygame.draw.rect(screen,color[1],input_rect6,3)
					text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(user_text,True,
						(255,255,255))
					screen.blit(text_surface,(input_rect6.x+11,input_rect6.y+5))
					last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(letter,
					 True, (255,255,255))
					screen.blit(last_letter, (1160, 495))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('word start with letter :',True,
						(255,255,255)),(420,490))
					if len(player_name[1])>0:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(player_name[1],True,
						(255,255,255)),(420,420))
					else:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAYER 2',True,
						(255,255,255)),(420,420))
					for i in range(8):
						if player_img[1][i]==True:
							screen.blit(pygame.transform.scale(face[i],(400,400)),(0,370))
						
			else:
				if winner_2==[1,0]:
					winner2=True
					break
				else:
					winner1=True
					break

			pygame.display.update()
			clock.tick(240)
		while players[0] and difficulty[2]:
			if my_timer3 != timer :
				timer=my_timer3
				if timer < 0:
					timer = 0
			time = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(str(timer).zfill(2), True, white)
			screen.blit(two_player_h[timer],(0,0))
			screen.blit(time, (717, 351))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE and len(user_text)>1:
						user_text = user_text[:-1]
					if event.key == pygame.K_BACKSPACE:
						pass
					elif event.key == pygame.K_RETURN:
						for i in range(144556):
							if t[i]==user_text:
								my_timer3 = 5
								if winner_2==[1,0]:
									letter = user_text[-1]
									user_text = letter
									winner_2=[0,1]
									my_timer3=5
								else:
									letter = user_text[-1]
									user_text = letter
									winner_2=[1,0]
									my_timer3=5
					else:
						if len(user_text)<20:
							user_text += event.unicode
			if timer!=0:
				if winner_2==[1,0]:
					screen.blit(playing1_2,(0,0))
					pygame.draw.rect(screen,color[1],input_rect5,3)
					text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(user_text,True,
						(255,255,255))
					screen.blit(text_surface,(input_rect5.x+11,input_rect5.y+5))
					last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(letter,
					 True, (255,255,255))
					screen.blit(last_letter, (1160, 115))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('word start with letter :',True,
						(255,255,255)),(420,110))
					if len(player_name[0])>0:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(player_name[0],True,
						(255,255,255)),(420,35))
					else:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAYER 1',True,
						(255,255,255)),(420,35))
					for i in range(8):
						if player_img[0][i]==True:
							screen.blit(pygame.transform.scale(face[i],(400,400)),(0,-5))
				else:
					screen.blit(playing2_2,(0,0))
					pygame.draw.rect(screen,color[1],input_rect6,3)
					text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(user_text,True,
						(255,255,255))
					screen.blit(text_surface,(input_rect6.x+11,input_rect6.y+5))
					last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(letter,
					 True, (255,255,255))
					screen.blit(last_letter, (1160, 495))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('word start with letter :',True,
						(255,255,255)),(420,490))
					if len(player_name[1])>0:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(player_name[1],True,
						(255,255,255)),(420,420))
					else:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAYER 2',True,
						(255,255,255)),(420,420))
					for i in range(8):
						if player_img[1][i]==True:
							screen.blit(pygame.transform.scale(face[i],(400,400)),(0,370))	
			else:
				if winner_2==[1,0]:
					winner2=True
					break
				elif winner_2==[0,1]:
					winner1=True
					break		
			
			pygame.display.update()
			clock.tick(240)
		while players[1] and difficulty[0]:
			if my_timer1 != timer :
				timer=my_timer1
				if timer < 0:
					timer = 0
			time = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(str(timer).zfill(2), True, white)
			screen.blit(three_player[timer],(0,0))
			screen.blit(time, (717, 351))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE and len(user_text)>1:
						user_text = user_text[:-1]
					if event.key == pygame.K_BACKSPACE:
						pass
					elif event.key == pygame.K_RETURN:
						for i in range(144556):
							if t[i]==user_text:								
								if winner_3==[1,-1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_3=[0,-1,1]
								elif winner_3==[1,0,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_3=[0,1,0]
								elif winner_3==[1,0,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_3=[0,1,-1]	
								elif winner_3==[-1,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_3=[-1,0,1]
								elif winner_3==[0,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_3=[0,0,1]
								elif winner_3==[0,1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_3=[1,0,-1]					
								elif winner_3==[-1,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_3=[-1,1,0]
								elif winner_3==[0,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_3=[1,0,0]
								elif winner_3==[0,-1,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_3=[1,-1,0]
					else:
						if len(user_text)<20:
							user_text += event.unicode
			if timer == 0:
				if winner_3==[1,0,0]:
					winner_3=[-1,1,0]
					my_timer1=20
				elif winner_3==[0,1,0] :
					winner_3=[0,-1,1]
					my_timer1=20
				elif winner_3==[0,0,1] :
					winner_3=[1,0,-1]
					my_timer1=20
				elif winner_3==[1,-1,0]:
					winner3=True
					break
				elif winner_3==[0,1,-1]:
					winner1=True
					break
				elif winner_3==[-1,1,0]:
					winner3=True
					break
				elif winner_3==[1,0,-1]:
					winner2=True
					break
				elif winner_3==[0,-1,1]:
					winner1=True
					break
				elif winner_3==[-1,0,1]:
					winner2=True
					break
					
			else :
				if winner_3[0]==1:
					screen.blit(playing1_2,(0,0))
					pygame.draw.rect(screen,color[1],input_rect5,3)
					text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(user_text,True,
						(255,255,255))
					screen.blit(text_surface,(input_rect5.x+11,input_rect5.y+5))
					last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(letter,
					 True, (255,255,255))
					screen.blit(last_letter, (1160, 115))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('word start with letter :',True,
						(255,255,255)),(420,110))
					if len(player_name[0])>0:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(player_name[0],True,
						(255,255,255)),(420,35))
					else:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAYER 1',True,
						(255,255,255)),(420,35))
					for i in range(8):
						if player_img[0][i]==True:
							screen.blit(pygame.transform.scale(face[i],(400,400)),(0,-5))
				elif winner_3[1]==1:
					screen.blit(playing3,(0,0))
					pygame.draw.rect(screen,color[1],input_rect7,3)
					text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
						(255,255,255))
					screen.blit(text_surface,(input_rect7.x+11,input_rect7.y))
					last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(letter,
					 True, (255,255,255))
					screen.blit(last_letter, (400, 550))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
						(255,255,255)),(250,500))
					if len(player_name[1])>0:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[1],True,
						(255,255,255)),(250,450))
					else:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 2',True,
						(255,255,255)),(250,450))
					for i in range(8):
						if player_img[0][i]==True:
							screen.blit(pygame.transform.scale(face[i],(250,250)),(0,400))
				elif winner_3[2]==1:
					screen.blit(playing4,(0,0))
					pygame.draw.rect(screen,color[1],input_rect8,3)
					text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
						(255,255,255))
					screen.blit(text_surface,(input_rect8.x+11,input_rect8.y))
					last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(letter,
					 True, (255,255,255))
					screen.blit(last_letter, (950, 550))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
						(255,255,255)),(780,500))
					if len(player_name[2])>0:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[2],True,
						(255,255,255)),(780,450))
					else:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 3',True,
						(255,255,255)),(780,450))
					for i in range(8):
						if player_img[0][i]==True:
							screen.blit(pygame.transform.scale(face[i],(250,250)),(1200,400))
			
			pygame.display.update()
			clock.tick(240)
		while players[1] and difficulty[1]:
			if my_timer2 != timer :
				timer=my_timer2
				if timer < 0:
					timer = 0
			time = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(str(timer).zfill(2), True, white)
			screen.blit(three_player_m[timer],(0,0))
			screen.blit(time, (717, 351))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE and len(user_text)>1:
						user_text = user_text[:-1]
					if event.key == pygame.K_BACKSPACE:
						pass
					elif event.key == pygame.K_RETURN:
						for i in range(144556):
							if t[i]==user_text:								
								if winner_3==[1,-1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_3=[0,-1,1]
								elif winner_3==[1,0,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_3=[0,1,0]
								elif winner_3==[1,0,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_3=[0,1,-1]	
								elif winner_3==[-1,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_3=[-1,0,1]
								elif winner_3==[0,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_3=[0,0,1]
								elif winner_3==[0,1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_3=[1,0,-1]					
								elif winner_3==[-1,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_3=[-1,1,0]
								elif winner_3==[0,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_3=[1,0,0]
								elif winner_3==[0,-1,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_3=[1,-1,0]
					else:
						if len(user_text)<20:
							user_text += event.unicode
			if timer == 0:
				print(winner_3)
				if winner_3==[1,0,0]:
					winner_3=[-1,1,0]
					my_timer2=10
				elif winner_3==[0,1,0] :
					winner_3=[0,-1,1]
					my_timer2=10
				elif winner_3==[0,0,1] :
					winner_3=[1,0,-1]
					my_timer2=10
				elif winner_3==[1,-1,0]:
					winner3=True
					break
				elif winner_3==[0,1,-1]:
					winner1=True
					break
				elif winner_3==[-1,1,0]:
					winner3=True
					break
				elif winner_3==[1,0,-1]:
					winner2=True
					break
				elif winner_3==[0,-1,1]:
					winner1=True
					break
				elif winner_3==[-1,0,1]:
					winner2=True
					break
					
			else :
				if winner_3[0]==1:
					screen.blit(playing1_2,(0,0))
					pygame.draw.rect(screen,color[1],input_rect5,3)
					text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(user_text,True,
						(255,255,255))
					screen.blit(text_surface,(input_rect5.x+11,input_rect5.y+5))
					last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(letter,
					 True, (255,255,255))
					screen.blit(last_letter, (1160, 115))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('word start with letter :',True,
						(255,255,255)),(420,110))
					if len(player_name[0])>0:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(player_name[0],True,
						(255,255,255)),(420,35))
					else:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAYER 1',True,
						(255,255,255)),(420,35))
					for i in range(8):
						if player_img[0][i]==True:
							screen.blit(pygame.transform.scale(face[i],(400,400)),(0,-5))
				elif winner_3[1]==1:
					screen.blit(playing3,(0,0))
					pygame.draw.rect(screen,color[1],input_rect7,3)
					text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
						(255,255,255))
					screen.blit(text_surface,(input_rect7.x+11,input_rect7.y))
					last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(letter,
					 True, (255,255,255))
					screen.blit(last_letter, (400, 500))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
						(255,255,255)),(250,450))
					for i in range(8):
						if player_img[0][i]==True:
							screen.blit(pygame.transform.scale(face[i],(250,250)),(0,400))
				elif winner_3[2]==1:
					screen.blit(playing4,(0,0))
					pygame.draw.rect(screen,color[1],input_rect8,3)
					text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
						(255,255,255))
					screen.blit(text_surface,(input_rect8.x+11,input_rect8.y))
					last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(letter,
					 True, (255,255,255))
					screen.blit(last_letter, (400, 550))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
						(255,255,255)),(250,500))
					if len(player_name[1])>0:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[1],True,
						(255,255,255)),(250,450))
					else:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 2',True,
						(255,255,255)),(250,450))
					for i in range(8):
						if player_img[0][i]==True:
							screen.blit(pygame.transform.scale(face[i],(250,250)),(1200,400))
			
			pygame.display.update()
			clock.tick(240)
		while players[1] and difficulty[2]:
			if my_timer3 != timer :
				timer=my_timer3
				if timer < 0:
					timer = 0
			time = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(str(timer).zfill(2), True, white)
			screen.blit(three_player_h[timer],(0,0))
			screen.blit(time, (717, 351))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE and len(user_text)>1:
						user_text = user_text[:-1]
					if event.key == pygame.K_BACKSPACE:
						pass
					elif event.key == pygame.K_RETURN:
						for i in range(144556):
							if t[i]==user_text:								
								if winner_3==[1,-1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_3=[0,-1,1]
								elif winner_3==[1,0,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_3=[0,1,0]
								elif winner_3==[1,0,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_3=[0,1,-1]	
								elif winner_3==[-1,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_3=[-1,0,1]
								elif winner_3==[0,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_3=[0,0,1]
								elif winner_3==[0,1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_3=[1,0,-1]					
								elif winner_3==[-1,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_3=[-1,1,0]
								elif winner_3==[0,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_3=[1,0,0]
								elif winner_3==[0,-1,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_3=[1,-1,0]
					else:
						if len(user_text)<20:
							user_text += event.unicode
			if timer == 0:
				if winner_3==[1,0,0]:
					winner_3=[-1,1,0]
					my_timer3=5
				elif winner_3==[0,1,0] :
					winner_3=[0,-1,1]
					my_timer3=5
				elif winner_3==[0,0,1] :
					winner_3=[1,0,-1]
					my_timer3=5
				elif winner_3==[1,-1,0]:
					winner3=True
					break
				elif winner_3==[0,1,-1]:
					winner1=True
					break
				elif winner_3==[-1,1,0]:
					winner3=True
					break
				elif winner_3==[1,0,-1]:
					winner2=True
					break
				elif winner_3==[0,-1,1]:
					winner1=True
					break
				elif winner_3==[-1,0,1]:
					print('yes')
					winner2=True
					break
					
			else :
				if winner_3[0]==1:
					screen.blit(playing1_2,(0,0))
					pygame.draw.rect(screen,color[1],input_rect5,3)
					text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(user_text,True,
						(255,255,255))
					screen.blit(text_surface,(input_rect5.x+11,input_rect5.y+5))
					last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(letter,
					 True, (255,255,255))
					screen.blit(last_letter, (1160, 115))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('word start with letter :',True,
						(255,255,255)),(420,110))
					if len(player_name[0])>0:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render(player_name[0],True,
						(255,255,255)),(420,35))
					else:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',60).render('PLAYER 1',True,
						(255,255,255)),(420,35))
					for i in range(8):
						if player_img[0][i]==True:
							screen.blit(pygame.transform.scale(face[i],(400,400)),(0,-5))
				elif winner_3[1]==1:
					screen.blit(playing3,(0,0))
					pygame.draw.rect(screen,color[1],input_rect7,3)
					text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
						(255,255,255))
					screen.blit(text_surface,(input_rect7.x+11,input_rect7.y))
					last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(letter,
					 True, (255,255,255))
					screen.blit(last_letter, (400, 550))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
						(255,255,255)),(250,500))
					if len(player_name[1])>0:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[1],True,
						(255,255,255)),(250,450))
					else:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 2',True,
						(255,255,255)),(250,450))
					for i in range(8):
						if player_img[0][i]==True:
							screen.blit(pygame.transform.scale(face[i],(250,250)),(0,400))
				elif winner_3[2]==1:
					screen.blit(playing4,(0,0))
					pygame.draw.rect(screen,color[1],input_rect8,3)
					text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
						(255,255,255))
					screen.blit(text_surface,(input_rect8.x+11,input_rect8.y))
					last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(letter,
					 True, (255,255,255))
					screen.blit(last_letter, (950, 550))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
						(255,255,255)),(780,500))
					if len(player_name[2])>0:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[2],True,
						(255,255,255)),(780,450))
					else:
						screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 3',True,
						(255,255,255)),(780,450))
					for i in range(8):
						if player_img[0][i]==True:
							screen.blit(pygame.transform.scale(face[i],(250,250)),(1200,400))
			
			pygame.display.update()
			clock.tick(240)
		while players[2] and difficulty[0]:
			if my_timer1 != timer :
				timer=my_timer1
				if timer < 0:
					timer = 0
			time = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(str(timer).zfill(2), True, white)
			screen.blit(four_player[timer],(0,0))
			screen.blit(time, (717, 351))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE and len(user_text)>1:
						user_text = user_text[:-1]
					if event.key == pygame.K_BACKSPACE:
						pass
					elif event.key == pygame.K_RETURN:
						for i in range(144556):
							if t[i]==user_text:								
								if winner_4==[1,-1,0,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[0,-1,1,0]
								elif winner_4==[1,-1,-1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[0,-1,-1,1]
								elif winner_4==[1,-1,0,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[0,-1,1,-1]
								elif winner_4==[1,0,-1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[0,1,-1,0]
								elif winner_4==[1,0,0,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[0,1,0,-1]
								elif winner_4==[1,0,-1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[0,1,-1,-1]
								elif winner_4==[-1,1,0,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[-1,0,1,0]
								elif winner_4==[-1,1,-1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[-1,0,-1,1]
								elif winner_4==[-1,1,0,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[-1,0,1,-1]
								elif winner_4==[0,1,-1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[0,0,-1,1]
								elif winner_4==[0,1,0,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[0,0,1,-1]
								elif winner_4==[0,1,-1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[1,0,-1,-1]
								elif winner_4==[-1,0,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[-1,0,0,1]
								elif winner_4==[-1,-1,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[-1,-1,0,1]
								elif winner_4==[0,-1,1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[1,-1,0,-1]
								elif winner_4==[-1,0,1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[-1,1,0,-1]
								elif winner_4==[0,-1,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[0,-1,0,1]
								elif winner_4==[0,0,1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[1,0,0,-1]
								elif winner_4==[-1,0,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[-1,1,0,0]
								elif winner_4==[-1,-1,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[-1,-1,1,0]
								elif winner_4==[0,-1,-1,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[1,-1,-1,0]
								elif winner_4==[-1,0,-1,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[-1,1,-1,0]
								elif winner_4==[0,-1,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[1,-1,0,0]
								elif winner_4==[0,0,-1,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[1,0,-1,0]
								elif winner_4==[1,0,0,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[0,1,0,0]
								elif winner_4==[0,1,0,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[0,0,1,0]
								elif winner_4==[0,0,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[0,0,0,1]
								elif winner_4==[0,0,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[1,0,0,0]
					else:
						if len(user_text)<20:
							user_text += event.unicode
			if timer == 0:
				if winner_4==[1,-1,0,0]:
					my_timer1=20
					winner_4=[-1,-1,1,0]
				elif winner_4==[1,-1,-1,0]:
					my_timer1=20
					winner_4=[-1,-1,-1,0]
				elif winner_4==[1,-1,0,-1]:
					my_timer1=20
					winner_4=[-1,-1,0,-1]
				elif winner_4==[1,0,-1,0]:
					my_timer1=20
					winner_4=[-1,1,-1,0]
				elif winner_4==[1,0,0,-1]:
					my_timer1=20
					winner_4=[-1,1,0,-1]
				elif winner_4==[1,0,-1,-1]:
					my_timer1=20
					winner_4=[-1,0,-1,-1]
				elif winner_4==[-1,1,0,0]:
					my_timer1=20
					winner_4=[-1,-1,1,0]
				elif winner_4==[-1,1,-1,0]:
					my_timer1=20
					winner_4=[-1,-1,-1,0]
				elif winner_4==[-1,1,0,-1]:
					my_timer1=20
					winner_4=[-1,-1,0,-1]
				elif winner_4==[0,1,-1,0]:
					my_timer1=20
					winner_4=[0,-1,-1,1]
				elif winner_4==[0,1,0,-1]:
					my_timer1=20
					winner_4=[0,-1,1,-1]
				elif winner_4==[0,1,-1,-1]:
					my_timer1=20
					winner_4=[0,-1,-1,-1]
				elif winner_4==[-1,0,1,0]:
					my_timer1=20
					winner_4=[-1,0,-1,1]
				elif winner_4==[-1,-1,1,0]:
					my_timer1=20
					winner_4=[-1,-1,-1,0]
				elif winner_4==[0,-1,1,-1]:
					my_timer1=20
					winner_4=[0,-1,-1,-1]
				elif winner_4==[-1,0,1,-1]:
					my_timer1=20
					winner_4=[-1,0,-1,-1]
				elif winner_4==[0,-1,1,0]:
					my_timer1=20
					winner_4=[0,-1,-1,1]
				elif winner_4==[0,0,1,-1]:
					my_timer1=20
					winner_4=[1,0,-1,-1]
				elif winner_4==[-1,0,0,1]:
					my_timer1=20
					winner_4=[-1,1,0,-1]
				elif winner_4==[-1,-1,0,1]:
					my_timer1=20
					winner_4=[-1,-1,0,-1]
				elif winner_4==[0,-1,-1,1]:
					my_timer1=20
					winner_4=[0,-1,-1,-1]
				elif winner_4==[-1,0,-1,1]:
					my_timer1=20
					winner_4=[-1,0,-1,-1]
				elif winner_4==[0,-1,0,1]:
					my_timer1=20
					winner_4=[1,-1,0,-1]
				elif winner_4==[0,0,-1,1]:
					my_timer1=20
					winner_4=[1,0,-1,-1]
				elif winner_4==[1,0,0,0]:
					my_timer1=20
					winner_4=[-1,1,0,0]
				elif winner_4==[0,1,0,0]:
					my_timer1=20
					winner_4=[0,-1,1,0]
				elif winner_4==[0,0,1,0]:
					my_timer1=20
					winner_4=[0,0,-1,1]
				elif winner_4==[0,0,0,1]:
					my_timer1=20
					winner_4=[1,0,0,-1]
				if winner_4==[-1, -1, -1, 0]:
					winner4=True
					break
				elif winner_4==[0, -1, -1, -1]:
					winner1=True
					break
				elif winner_4==[-1, 0, -1, -1]:
					winner2=True
					break
				elif winner_4==[-1,-1, 0,-1]:
					winner3=True
					break	
			if winner_4[0]==1:
				screen.blit(playing1,(0,0))
				pygame.draw.rect(screen,color[1],input_rect9,3)
				text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
					(255,255,255))
				screen.blit(text_surface,(input_rect9.x+11,input_rect9.y))
				last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(letter,
					 True, (255,255,255))
				screen.blit(last_letter, (400, 150))
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
					(255,255,255)),(250,100))
				if len(player_name[0])>0:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[0],True,
					(255,255,255)),(250,50))
				else:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 1',True,
					(255,255,255)),(250,50))
				for i in range(8):
					if player_img[0][i]==True:
						screen.blit(pygame.transform.scale(face[i],(250,250)),(0,0))
			elif winner_4[2]==1:
				screen.blit(playing3,(0,0))
				pygame.draw.rect(screen,color[1],input_rect7,3)
				text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
					(255,255,255))
				screen.blit(text_surface,(input_rect7.x+11,input_rect7.y))
				last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(letter,
				 True, (255,255,255))
				screen.blit(last_letter, (400, 530))
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
					(255,255,255)),(250,500))
				if len(player_name[2])>0:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[2],True,
					(255,255,255)),(250,450))
				else:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 3',True,
					(255,255,255)),(250,450))
				for i in range(8):
					if player_img[2][i]==True:
						screen.blit(pygame.transform.scale(face[i],(250,250)),(0,400))
			elif winner_4[3]==1:
				screen.blit(playing4,(0,0))
				pygame.draw.rect(screen,color[1],input_rect8,3)
				text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
					(255,255,255))
				screen.blit(text_surface,(input_rect8.x+11,input_rect8.y))
				last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(letter,
				 True, (255,255,255))
				screen.blit(last_letter, (950, 530))
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
					(255,255,255)),(780,500))
				if len(player_name[3])>0:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[3],True,
					(255,255,255)),(780,450))
				else:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 4',True,
					(255,255,255)),(780,450))
				for i in range(8):
					if player_img[3][i]==True:
						screen.blit(pygame.transform.scale(face[i],(250,250)),(1200,400))
			elif winner_4[1]==1:
				screen.blit(playing2,(0,0))
				pygame.draw.rect(screen,color[1],input_rect10,3)
				text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
					(255,255,255))
				screen.blit(text_surface,(input_rect10.x+11,input_rect10.y))
				last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(letter,
				 True, (255,255,255))
				screen.blit(last_letter, (950, 150))
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
					(255,255,255)),(780,100))
				if len(player_name[1])>0:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[1],True,
					(255,255,255)),(780,50))
				else:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 2',True,
					(255,255,255)),(780,50))
				for i in range(8):
					if player_img[1][i]==True:
						screen.blit(pygame.transform.scale(face[i],(250,250)),(1200,0))
			pygame.display.update()
			clock.tick(240)
		while players[2] and difficulty[1]:
			if my_timer2 != timer :
				timer=my_timer2
				if timer < 0:
					timer = 0
			time = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(str(timer).zfill(2), True, white)
			screen.blit(four_player_m[timer],(0,0))
			screen.blit(time, (717, 351))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE and len(user_text)>1:
						user_text = user_text[:-1]
					if event.key == pygame.K_BACKSPACE:
						pass
					elif event.key == pygame.K_RETURN:
						for i in range(144556):
							if t[i]==user_text:								
								if winner_4==[1,-1,0,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[0,-1,1,0]
								elif winner_4==[1,-1,-1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[0,-1,-1,1]
								elif winner_4==[1,-1,0,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[0,-1,1,-1]
								elif winner_4==[1,0,-1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[0,1,-1,0]
								elif winner_4==[1,0,0,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[0,1,0,-1]
								elif winner_4==[1,0,-1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[0,1,-1,-1]
								elif winner_4==[-1,1,0,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[-1,0,1,0]
								elif winner_4==[-1,1,-1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[-1,0,-1,1]
								elif winner_4==[-1,1,0,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[-1,0,1,-1]
								elif winner_4==[0,1,-1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[0,0,-1,1]
								elif winner_4==[0,1,0,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[0,0,1,-1]
								elif winner_4==[0,1,-1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[1,0,-1,-1]
								elif winner_4==[-1,0,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[-1,0,0,1]
								elif winner_4==[-1,-1,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[-1,-1,0,1]
								elif winner_4==[0,-1,1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[1,-1,0,-1]
								elif winner_4==[-1,0,1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[-1,1,0,-1]
								elif winner_4==[0,-1,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[0,-1,0,1]
								elif winner_4==[0,0,1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[1,0,0,-1]
								elif winner_4==[-1,0,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[-1,1,0,0]
								elif winner_4==[-1,-1,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[-1,-1,1,0]
								elif winner_4==[0,-1,-1,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[1,-1,-1,0]
								elif winner_4==[-1,0,-1,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[-1,1,-1,0]
								elif winner_4==[0,-1,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[1,-1,0,0]
								elif winner_4==[0,0,-1,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[1,0,-1,0]
								elif winner_4==[1,0,0,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[0,1,0,0]
								elif winner_4==[0,1,0,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[0,0,1,0]
								elif winner_4==[0,0,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[0,0,0,1]
								elif winner_4==[0,0,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer2=10
									winner_4=[1,0,0,0]
					else:
						if len(user_text)<20:
							user_text += event.unicode
			if timer == 0:
				if winner_4==[1,-1,0,0]:
					my_timer2=10
					winner_4=[-1,-1,1,0]
				elif winner_4==[1,-1,-1,0]:
					my_timer2=10
					winner_4=[-1,-1,-1,0]
				elif winner_4==[1,-1,0,-1]:
					my_timer2=10
					winner_4=[-1,-1,0,-1]
				elif winner_4==[1,0,-1,0]:
					my_timer2=10
					winner_4=[-1,1,-1,0]
				elif winner_4==[1,0,0,-1]:
					my_timer2=10
					winner_4=[-1,1,0,-1]
				elif winner_4==[1,0,-1,-1]:
					my_timer2=10
					winner_4=[-1,0,-1,-1]
				elif winner_4==[-1,1,0,0]:
					my_timer2=10
					winner_4=[-1,-1,1,0]
				elif winner_4==[-1,1,-1,0]:
					my_timer2=10
					winner_4=[-1,-1,-1,0]
				elif winner_4==[-1,1,0,-1]:
					my_timer2=10
					winner_4=[-1,-1,0,-1]
				elif winner_4==[0,1,-1,0]:
					my_timer2=10
					winner_4=[0,-1,-1,1]
				elif winner_4==[0,1,0,-1]:
					my_timer2=10
					winner_4=[0,-1,1,-1]
				elif winner_4==[0,1,-1,-1]:
					my_timer2=10
					winner_4=[0,-1,-1,-1]
				elif winner_4==[-1,0,1,0]:
					my_timer2=10
					winner_4=[-1,0,-1,1]
				elif winner_4==[-1,-1,1,0]:
					my_timer2=10
					winner_4=[-1,-1,-1,0]
				elif winner_4==[0,-1,1,-1]:
					my_timer2=10
					winner_4=[0,-1,-1,-1]
				elif winner_4==[-1,0,1,-1]:
					my_timer2=10
					winner_4=[-1,0,-1,-1]
				elif winner_4==[0,-1,1,0]:
					my_timer2=10
					winner_4=[0,-1,-1,1]
				elif winner_4==[0,0,1,-1]:
					my_timer2=10
					winner_4=[1,0,-1,-1]
				elif winner_4==[-1,0,0,1]:
					my_timer2=10
					winner_4=[-1,1,0,-1]
				elif winner_4==[-1,-1,0,1]:
					my_timer2=10
					winner_4=[-1,-1,0,-1]
				elif winner_4==[0,-1,-1,1]:
					my_timer2=10
					winner_4=[0,-1,-1,-1]
				elif winner_4==[-1,0,-1,1]:
					my_timer2=10
					winner_4=[-1,0,-1,-1]
				elif winner_4==[0,-1,0,1]:
					my_timer2=10
					winner_4=[1,-1,0,-1]
				elif winner_4==[0,0,-1,1]:
					my_timer2=10
					winner_4=[1,0,-1,-1]
				elif winner_4==[1,0,0,0]:
					my_timer2=10
					winner_4=[-1,1,0,0]
				elif winner_4==[0,1,0,0]:
					my_timer2=10
					winner_4=[0,-1,1,0]
				elif winner_4==[0,0,1,0]:
					my_timer2=10
					winner_4=[0,0,-1,1]
				elif winner_4==[0,0,0,1]:
					my_timer2=10
					winner_4=[1,0,0,-1]
				if winner_4==[-1, -1, -1, 0]:
					winner4=True
					break
				elif winner_4==[0, -1, -1, -1]:
					winner1=True
					break
				elif winner_4==[-1, 0, -1, -1]:
					winner2=True
					break
				elif winner_4==[-1,-1, 0,-1]:
					winner3=True
					break	
			if winner_4[0]==1:
				screen.blit(playing1,(0,0))
				pygame.draw.rect(screen,color[1],input_rect9,3)
				text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
					(255,255,255))
				screen.blit(text_surface,(input_rect9.x+11,input_rect9.y))
				last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(letter,
				 True, (255,255,255))
				screen.blit(last_letter, (400, 150))
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
					(255,255,255)),(250,100))
				if len(player_name[0])>0:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[0],True,
					(255,255,255)),(250,50))
				else:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 1',True,
					(255,255,255)),(250,50))
				for i in range(8):
					if player_img[0][i]==True:
						screen.blit(pygame.transform.scale(face[i],(250,250)),(0,0))
			elif winner_4[2]==1:
				screen.blit(playing3,(0,0))
				pygame.draw.rect(screen,color[1],input_rect7,3)
				text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
					(255,255,255))
				screen.blit(text_surface,(input_rect7.x+11,input_rect7.y))
				last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(letter,
				 True, (255,255,255))
				screen.blit(last_letter, (400, 530))
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
					(255,255,255)),(250,500))
				if len(player_name[2])>0:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[2],True,
					(255,255,255)),(250,450))
				else:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 3',True,
					(255,255,255)),(250,450))
				for i in range(8):
					if player_img[2][i]==True:
						screen.blit(pygame.transform.scale(face[i],(250,250)),(0,400))
			elif winner_4[3]==1:
				screen.blit(playing4,(0,0))
				pygame.draw.rect(screen,color[1],input_rect8,3)
				text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
					(255,255,255))
				screen.blit(text_surface,(input_rect8.x+11,input_rect8.y))
				last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(letter,
				 True, (255,255,255))
				screen.blit(last_letter, (950, 530))
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
					(255,255,255)),(780,500))
				if len(player_name[3])>0:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[3],True,
					(255,255,255)),(780,450))
				else:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 4',True,
					(255,255,255)),(780,450))
				for i in range(8):
					if player_img[3][i]==True:
						screen.blit(pygame.transform.scale(face[i],(250,250)),(1200,400))
			elif winner_4[1]==1:
				screen.blit(playing2,(0,0))
				pygame.draw.rect(screen,color[1],input_rect10,3)
				text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
					(255,255,255))
				screen.blit(text_surface,(input_rect10.x+11,input_rect10.y))
				last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(letter,
				 True, (255,255,255))
				screen.blit(last_letter, (950, 150))
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
					(255,255,255)),(780,100))
				if len(player_name[1])>0:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[1],True,
					(255,255,255)),(780,50))
				else:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 2',True,
					(255,255,255)),(780,50))
				for i in range(8):
					if player_img[1][i]==True:
						screen.blit(pygame.transform.scale(face[i],(250,250)),(1200,0))
			pygame.display.update()
			clock.tick(240)
		while players[2] and difficulty[2]:
			if my_timer3 != timer :
				timer=my_timer3
				if timer < 0:
					timer = 0
			time = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render(str(timer).zfill(2), True, white)
			screen.blit(four_player_h[timer],(0,0))
			screen.blit(time, (717, 351))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE and len(user_text)>1:
						user_text = user_text[:-1]
					if event.key == pygame.K_BACKSPACE:
						pass
					elif event.key == pygame.K_RETURN:
						for i in range(144556):
							if t[i]==user_text:								
								if winner_4==[1,-1,0,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[0,-1,1,0]
								elif winner_4==[1,-1,-1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[0,-1,-1,1]
								elif winner_4==[1,-1,0,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[0,-1,1,-1]
								elif winner_4==[1,0,-1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[0,1,-1,0]
								elif winner_4==[1,0,0,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[0,1,0,-1]
								elif winner_4==[1,0,-1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[0,1,-1,-1]
								elif winner_4==[-1,1,0,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[-1,0,1,0]
								elif winner_4==[-1,1,-1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[-1,0,-1,1]
								elif winner_4==[-1,1,0,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[-1,0,1,-1]
								elif winner_4==[0,1,-1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[0,0,-1,1]
								elif winner_4==[0,1,0,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[0,0,1,-1]
								elif winner_4==[0,1,-1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[1,0,-1,-1]
								elif winner_4==[-1,0,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[-1,0,0,1]
								elif winner_4==[-1,-1,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[-1,-1,0,1]
								elif winner_4==[0,-1,1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[1,-1,0,-1]
								elif winner_4==[-1,0,1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[-1,1,0,-1]
								elif winner_4==[0,-1,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[0,-1,0,1]
								elif winner_4==[0,0,1,-1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[1,0,0,-1]
								elif winner_4==[-1,0,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[-1,1,0,0]
								elif winner_4==[-1,-1,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[-1,-1,1,0]
								elif winner_4==[0,-1,-1,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer1=20
									winner_4=[1,-1,-1,0]
								elif winner_4==[-1,0,-1,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[-1,1,-1,0]
								elif winner_4==[0,-1,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[1,-1,0,0]
								elif winner_4==[0,0,-1,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[1,0,-1,0]
								elif winner_4==[1,0,0,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[0,1,0,0]
								elif winner_4==[0,1,0,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[0,0,1,0]
								elif winner_4==[0,0,1,0]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[0,0,0,1]
								elif winner_4==[0,0,0,1]:
									letter = user_text[-1]
									user_text = letter
									my_timer3=5
									winner_4=[1,0,0,0]
					else:
						if len(user_text)<20:
							user_text += event.unicode
			if timer == 0:
				if winner_4==[1,-1,0,0]:
					my_timer3=5
					winner_4=[-1,-1,1,0]
				elif winner_4==[1,-1,-1,0]:
					my_timer3=5
					winner_4=[-1,-1,-1,0]
				elif winner_4==[1,-1,0,-1]:
					my_timer3=5
					winner_4=[-1,-1,0,-1]
				elif winner_4==[1,0,-1,0]:
					my_timer3=5
					winner_4=[-1,1,-1,0]
				elif winner_4==[1,0,0,-1]:
					my_timer3=5
					winner_4=[-1,1,0,-1]
				elif winner_4==[1,0,-1,-1]:
					my_timer3=5
					winner_4=[-1,0,-1,-1]
				elif winner_4==[-1,1,0,0]:
					my_timer3=5
					winner_4=[-1,-1,1,0]
				elif winner_4==[-1,1,-1,0]:
					my_timer3=5
					winner_4=[-1,-1,-1,0]
				elif winner_4==[-1,1,0,-1]:
					my_timer3=5
					winner_4=[-1,-1,0,-1]
				elif winner_4==[0,1,-1,0]:
					my_timer3=5
					winner_4=[0,-1,-1,1]
				elif winner_4==[0,1,0,-1]:
					my_timer3=5
					winner_4=[0,-1,1,-1]
				elif winner_4==[0,1,-1,-1]:
					my_timer3=5
					winner_4=[0,-1,-1,-1]
				elif winner_4==[-1,0,1,0]:
					my_timer3=5
					winner_4=[-1,0,-1,1]
				elif winner_4==[-1,-1,1,0]:
					my_timer3=5
					winner_4=[-1,-1,-1,0]
				elif winner_4==[0,-1,1,-1]:
					my_timer3=5
					winner_4=[0,-1,-1,-1]
				elif winner_4==[-1,0,1,-1]:
					my_timer3=5
					winner_4=[-1,0,-1,-1]
				elif winner_4==[0,-1,1,0]:
					my_timer3=5
					winner_4=[0,-1,-1,1]
				elif winner_4==[0,0,1,-1]:
					my_timer3=5
					winner_4=[1,0,-1,-1]
				elif winner_4==[-1,0,0,1]:
					my_timer3=5
					winner_4=[-1,1,0,-1]
				elif winner_4==[-1,-1,0,1]:
					my_timer3=5
					winner_4=[-1,-1,0,-1]
				elif winner_4==[0,-1,-1,1]:
					my_timer3=5
					winner_4=[0,-1,-1,-1]
				elif winner_4==[-1,0,-1,1]:
					my_timer3=5
					winner_4=[-1,0,-1,-1]
				elif winner_4==[0,-1,0,1]:
					my_timer3=5
					winner_4=[1,-1,0,-1]
				elif winner_4==[0,0,-1,1]:
					my_timer3=5
					winner_4=[1,0,-1,-1]
				elif winner_4==[1,0,0,0]:
					my_timer3=5
					winner_4=[-1,1,0,0]
				elif winner_4==[0,1,0,0]:
					my_timer3=5
					winner_4=[0,-1,1,0]
				elif winner_4==[0,0,1,0]:
					my_timer3=5
					winner_4=[0,0,-1,1]
				elif winner_4==[0,0,0,1]:
					my_timer3=5
					winner_4=[1,0,0,-1]
				if winner_4==[-1, -1, -1, 0]:
					winner4=True
					break
				elif winner_4==[0, -1, -1, -1]:
					winner1=True
					break
				elif winner_4==[-1, 0, -1, -1]:
					winner2=True
					break
				elif winner_4==[-1,-1, 0,-1]:
					winner3=True
					break	
			if winner_4[0]==1:
				screen.blit(playing1,(0,0))
				pygame.draw.rect(screen,color[1],input_rect9,3)
				text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
					(255,255,255))
				screen.blit(text_surface,(input_rect9.x+11,input_rect9.y))
				last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(letter,
					 True, (255,255,255))
				screen.blit(last_letter, (400, 150))
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
					(255,255,255)),(250,100))
				if len(player_name[0])>0:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[0],True,
					(255,255,255)),(250,50))
				else:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 1',True,
					(255,255,255)),(250,50))
				for i in range(8):
					if player_img[0][i]==True:
						screen.blit(pygame.transform.scale(face[i],(250,250)),(0,0))
			elif winner_4[2]==1:
				screen.blit(playing3,(0,0))
				pygame.draw.rect(screen,color[1],input_rect7,3)
				text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
					(255,255,255))
				screen.blit(text_surface,(input_rect7.x+11,input_rect7.y))
				last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(letter,
				 True, (255,255,255))
				screen.blit(last_letter, (400, 530))
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
					(255,255,255)),(250,500))
				if len(player_name[2])>0:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[2],True,
					(255,255,255)),(250,450))
				else:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 3',True,
					(255,255,255)),(250,450))
				for i in range(8):
					if player_img[2][i]==True:
						screen.blit(pygame.transform.scale(face[i],(250,250)),(0,400))
			elif winner_4[3]==1:
				screen.blit(playing4,(0,0))
				pygame.draw.rect(screen,color[1],input_rect8,3)
				text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
					(255,255,255))
				screen.blit(text_surface,(input_rect8.x+11,input_rect8.y))
				last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(letter,
				 True, (255,255,255))
				screen.blit(last_letter, (950, 530))
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
					(255,255,255)),(780,500))
				if len(player_name[3])>0:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[3],True,
					(255,255,255)),(780,450))
				else:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 4',True,
					(255,255,255)),(780,450))
				for i in range(8):
					if player_img[3][i]==True:
						screen.blit(pygame.transform.scale(face[i],(250,250)),(1200,400))
			elif winner_4[1]==1:
				screen.blit(playing2,(0,0))
				pygame.draw.rect(screen,color[1],input_rect10,3)
				text_surface = pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',55).render(user_text,True,
					(255,255,255))
				screen.blit(text_surface,(input_rect10.x+11,input_rect10.y))
				last_letter =  pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(letter,
				 True, (255,255,255))
				screen.blit(last_letter, (950, 150))
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('word start with letter :',True,
					(255,255,255)),(780,100))
				if len(player_name[1])>0:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render(player_name[1],True,
					(255,255,255)),(780,50))
				else:
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',30).render('PLAYER 2',True,
					(255,255,255)),(780,50))
				for i in range(8):
					if player_img[1][i]==True:
						screen.blit(pygame.transform.scale(face[i],(250,250)),(1200,0))
			pygame.display.update()
			clock.tick(240)
		while winner1:
			screen.blit(loading,(0,0))
			for i in range(8):
				if player_img[0][i]==True:
					screen.blit(pygame.transform.scale(face[i],(400,400)),(550,10))
			if len(player_name[0])>0:
				player_win=[]
				player_win.append(player_name[0]+' WIN')
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(player_win[0],True,
				(255,255,255)),(570,400))
			else:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render('PLAYER 1 WIN',True,
				(255,255,255)),(550,400))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if main_menu.draw_button() :
					click.play()
					screen.blit(pygame.transform.scale(m_button_pressed, (450, 95)),(270,550))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('< MAIN MENU',True,
					(255,255,255)),(350,569))
					player_win=[]
					winner_4 =[1,0,0,0]
					winner_3=[1,0,0]
					winner_2=[1,0]
					my_timer2=10
					my_timer1= 20
					my_timer3= 5
					letter =chr(randint(97,120))
					user_text = letter
					winner1=False
					game[2]=False
					game[0]=True
					Menu[0]=True
				if play_again.draw_button():
					click.play()
					screen.blit(pygame.transform.scale(m_button, (450, 95)),(780,550))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('PLAY AGAIN >',True,
					(255,255,255)),(855,569))
					player_win=[]
					winner_4 =[1,0,0,0]
					winner_3=[1,0,0]
					winner_2=[1,0]
					my_timer2=10
					my_timer1= 20
					my_timer3= 5
					letter =chr(randint(97,120))
					user_text = letter
					winner1=False
			screen.blit(pygame.transform.scale(m_button, (450, 95)),(780,550))
			play_again.draw_button()
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('PLAY AGAIN >',True,
				(255,255,255)),(855,569))
			screen.blit(pygame.transform.scale(m_button, (450, 95)),(270,550))
			main_menu.draw_button()
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('< MAIN MENU',True,
				(255,255,255)),(350,569))
			pygame.display.update()
			clock.tick(240)
		while winner2:
			screen.blit(loading,(0,0))
			for i in range(8):
				if player_img[1][i]==True:
					screen.blit(pygame.transform.scale(face[i],(400,400)),(550,10))
			if len(player_name[1])>0:
				player_win=[]
				player_win.append(player_name[1]+' WIN')
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(player_win[0],True,
				(255,255,255)),(570,400))
			else:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render('PLAYER 2 WIN',True,
				(255,255,255)),(550,400))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if main_menu.draw_button() :
					click.play()
					screen.blit(pygame.transform.scale(m_button_pressed, (450, 95)),(270,550))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('< MAIN MENU',True,
					(255,255,255)),(350,569))
					player_win=[]
					winner_4 =[1,0,0,0]
					winner_3=[1,0,0]
					winner_2=[1,0]
					my_timer2=10
					my_timer1= 20
					my_timer3= 5
					letter =chr(randint(97,120))
					user_text = letter
					winner2=False
					game[2]=False
					game[0]=True
					Menu[0]=True
				if play_again.draw_button():
					click.play()
					screen.blit(pygame.transform.scale(m_button, (450, 95)),(780,550))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('PLAY AGAIN >',True,
					(255,255,255)),(855,569))
					player_win=[]
					winner_4 =[1,0,0,0]
					winner_3=[1,0,0]
					winner_2=[1,0]
					my_timer2=10
					my_timer1= 20
					my_timer3= 5
					letter =chr(randint(97,120))
					user_text = letter
					winner2=False
			screen.blit(pygame.transform.scale(m_button, (450, 95)),(780,550))
			play_again.draw_button()
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('PLAY AGAIN >',True,
				(255,255,255)),(855,569))
			screen.blit(pygame.transform.scale(m_button, (450, 95)),(270,550))
			main_menu.draw_button()
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('< MAIN MENU',True,
				(255,255,255)),(350,569))
			pygame.display.update()
			clock.tick(240)
		while winner3:
			screen.blit(loading,(0,0))
			for i in range(8):
				if player_img[0][i]==True:
					screen.blit(pygame.transform.scale(face[i],(400,400)),(550,10))
			if len(player_name[2])>0:
				player_win=[]
				player_win.append(player_name[2]+' WIN')
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(player_win[0],True,
				(255,255,255)),(570,400))
			else:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render('PLAYER 3 WIN',True,
				(255,255,255)),(550,400))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if main_menu.draw_button() :
					click.play()
					screen.blit(pygame.transform.scale(m_button_pressed, (450, 95)),(270,550))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('< MAIN MENU',True,
					(255,255,255)),(350,569))
					player_win=[]
					winner_4 =[1,0,0,0]
					winner_3=[1,0,0]
					winner_2=[1,0]
					my_timer2=10
					my_timer1= 20
					my_timer3= 5
					letter =chr(randint(97,120))
					user_text = letter
					winner3=False
					game[2]=False
					game[0]=True
					Menu[0]=True
				if play_again.draw_button():
					click.play()
					screen.blit(pygame.transform.scale(m_button, (450, 95)),(780,550))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('PLAY AGAIN >',True,
					(255,255,255)),(855,569))
					player_win=[]
					winner_4 =[1,0,0,0]
					winner_3=[1,0,0]
					winner_2=[1,0]
					my_timer2=10
					my_timer1= 20
					my_timer3= 5
					letter =chr(randint(97,120))
					user_text = letter
					winner3=False
			screen.blit(pygame.transform.scale(m_button, (450, 95)),(780,550))
			play_again.draw_button()
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('PLAY AGAIN >',True,
				(255,255,255)),(855,569))
			screen.blit(pygame.transform.scale(m_button, (450, 95)),(270,550))
			main_menu.draw_button()
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('< MAIN MENU',True,
				(255,255,255)),(350,569))
			pygame.display.update()
			clock.tick(240)
		while winner4:
			screen.blit(loading,(0,0))
			for i in range(8):
				if player_img[0][i]==True:
					screen.blit(pygame.transform.scale(face[i],(400,400)),(550,10))
			if len(player_name[3])>0:
				player_win=[]
				player_win.append(player_name[3]+' WIN')
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render(player_win[0],True,
				(255,255,255)),(570,400))
			else:
				screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',70).render('PLAYER 4 WIN',True,
				(255,255,255)),(550,400))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game = False
					pygame.quit()
					sys.exit()
				if main_menu.draw_button() :
					click.play()
					screen.blit(pygame.transform.scale(m_button_pressed, (450, 95)),(270,550))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('< MAIN MENU',True,
					(255,255,255)),(350,569))
					player_win=[]
					winner_4 =[1,0,0,0]
					winner_3=[1,0,0]
					winner_2=[1,0]
					my_timer2=10
					my_timer1= 20
					my_timer3= 5
					letter =chr(randint(97,120))
					user_text = letter
					winner4=False
					game[2]=False
					game[0]=True
					Menu[0]=True
				if play_again.draw_button():
					click.play()
					screen.blit(pygame.transform.scale(m_button, (450, 95)),(780,550))
					screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('PLAY AGAIN >',True,
					(255,255,255)),(855,569))
					player_win=[]
					winner_4 =[1,0,0,0]
					winner_3=[1,0,0]
					winner_2=[1,0]
					my_timer2=10
					my_timer1= 20
					my_timer3= 5
					letter =chr(randint(97,120))
					user_text = letter
					winner4=False
			screen.blit(pygame.transform.scale(m_button, (450, 95)),(780,550))
			play_again.draw_button()
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('PLAY AGAIN >',True,
				(255,255,255)),(855,569))
			screen.blit(pygame.transform.scale(m_button, (450, 95)),(270,550))
			main_menu.draw_button()
			screen.blit( pygame.font.Font('.\data\dfont\iFlash 502 Regular.ttf',50).render('< MAIN MENU',True,
				(255,255,255)),(350,569))
			pygame.display.update()
			clock.tick(240)
		pygame.display.update()
		clock.tick(240)