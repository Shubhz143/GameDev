import pygame
import random
pygame.init()

white =(255,255,255)
black =(0,0,0)
red =(255,0,0)
green=(0,155,0)
display_width=800
display_height=600

gameDisplay =pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

snakeHeadImg= pygame.image.load('snakeHead.png')
appleImg=pygame.image.load('Apple.png')

clock=pygame.time.Clock()
block_size = 20
FPS = 30

direction="right"

smallFont =pygame.font.SysFont("comicsansms",25)
midFont =pygame.font.SysFont("comicsansms",50)
largeFont =pygame.font.SysFont("comicsansms",80)


def game_intro():
	intro="True"
	while intro:
		for event in pygame.event.get():
				if event.type ==pygame.QUIT:
					pygame.quit()
					quit()
				if event.type ==pygame.KEYDOWN:
					if event.key== pygame.K_q:
						pygame.quit()
						quit()
					if event.key==pygame.K_c:
						intro=False
		gameDisplay.fill(white)
		message_to_screen("Welcome to Slither",
						   green,
						   -100,
						   "large")
		message_to_screen("The objective of game is to eat red apples",
						   black,
						   -30)
		message_to_screen("The more apple you eat, the longer you get",
						   black,
						   10)
		message_to_screen("If you run into yourself, or the edge you die!!!",
						   black,
						   50)

		message_to_screen("Press C to play or Q to Quit.",
						   black,
						   180)
		pygame.display.update()
		clock.tick(4)
def snake(block_size,snakeList):
	if direction=="right":
		head = pygame.transform.rotate(snakeHeadImg,270)
	if direction=="left":
		head = pygame.transform.rotate(snakeHeadImg,90)
	if direction=="up":
		head = snakeHeadImg
	if direction=="down":
		head = pygame.transform.rotate(snakeHeadImg,180)
	gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))
	for XnY in snakeList[:-1]:
		pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
	if size=="small":
		textSurface=smallFont.render(text,True,color)
	elif size=="midium":
		textSurface=midFont.render(text,True,color)	
	elif size=="large":
		textSurface=largeFont.render(text,True,color)
	
	return textSurface, textSurface.get_rect()


def message_to_screen(msg,color,y_Displace=0,size="small"):
	textSurf,textRect = text_objects(msg,color,size)
	textRect.center= (display_width/2),(display_height/2)+y_Displace
	gameDisplay.blit(textSurf,textRect)

def gameLoop():
	global direction
	gameExit=False
	gameOver=False
	lead_X = display_width/2
	lead_Y = display_height/2
	lead_X_change=10
	lead_Y_change=0
	snakeList=[]
	snakelength = 1
	randAppleX=round(random.randrange(0,display_width-block_size))
	randAppleY=round(random.randrange(0,display_height-block_size))
	while not gameExit:

		while gameOver==True:
			gameDisplay.fill(white)
			message_to_screen("Game Over ",
							red, 
							y_Displace=-50,
							size="large")
			message_to_screen("Press C to Play again or Q to Quit",
							black,
							y_Displace=50,
							size="midium")
			pygame.display.update()
			for event in pygame.event.get():
				if event.type ==pygame.QUIT:
					gameExit=True
					gameOver=False
				if event.type ==pygame.KEYDOWN:
					if event.key== pygame.K_q:
						gameExit=True
						gameOver=False

					if event.key==pygame.K_c:
						gameLoop()
		for event in pygame.event.get():
			if event.type ==pygame.QUIT:
				gameExit=True
			if event.type ==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					lead_X_change =-block_size
					lead_Y_change = 0
					direction="left"
				elif event.key==pygame.K_RIGHT:
					lead_X_change =block_size
					lead_Y_change = 0
					direction="right"
				elif event.key==pygame.K_UP:
					lead_Y_change =-block_size
					lead_X_change =0
					direction="up"
				elif event.key==pygame.K_DOWN:
					lead_Y_change =block_size
					lead_X_change =0
					direction="down"
		if lead_X >=display_width or lead_X <0 or lead_Y >=display_height  or lead_Y <0:
			gameOver=True
		lead_X+=lead_X_change
		lead_Y+=lead_Y_change
		appleThickness=30


		gameDisplay.fill(white)
		gameDisplay.blit(appleImg,(randAppleX,randAppleY))
		
		snakeHead=[]
		snakeHead.append(lead_X)
		snakeHead.append(lead_Y)
		snakeList.append(snakeHead)
		if len(snakeList) > snakelength:
			del snakeList[0]
		for eachSegment in snakeList[:-1]:
			if eachSegment==snakeHead:
				gameOver=True

		snake(block_size,snakeList)
		pygame.display.update()
	
		if lead_X > randAppleX and lead_X < randAppleX + appleThickness or lead_X + block_size > randAppleX and lead_X + block_size < randAppleX + appleThickness:
			if lead_Y > randAppleY and lead_Y < randAppleY + appleThickness or lead_Y + block_size > randAppleY and lead_Y + block_size < randAppleY + appleThickness:
				snakelength+=1
				randAppleX=round(random.randrange(0,display_width-block_size))
				randAppleY=round(random.randrange(0,display_height-block_size))
		clock.tick(FPS)
	pygame.quit()
	quit()

game_intro()
gameLoop()
