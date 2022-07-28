import pygame, sys
from pygame.locals import *
pygame.init()

WINDOWWIDTH = 500
WINDOWHEIGHT = 600

FPS = 60
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('xe oto')
LIGHTBLUE = (92, 161, 255)



RED = (255, 0 , 0)
LIGHTPINK = (253, 68, 255)
BLACK = (0, 0, 0)
running = True

car_x = 0
car_y = 200
carSurface = pygame.Surface((100, 50),SRCALPHA)
pygame.draw.circle(carSurface, BLACK, (25,43.25), 6.75)
pygame.draw.circle(carSurface, BLACK, (75, 43.25), 6.75)
pygame.draw.polygon(carSurface, RED, ((25,25),(50,12.5),(75,25),(75,37.5),(25,37.5)))



while running:
	screen.fill(LIGHTBLUE)
	screen.blit(carSurface, (car_x, car_y))
	
			

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	car_x +=2
	if car_x + 100 > WINDOWWIDTH:
		car_x = WINDOWWIDTH - 100

		if car_x == WINDOWWIDTH - 100:
			car_y +=2
			if car_y+60 > WINDOWHEIGHT:
				car_y = WINDOWHEIGHT-60




	
	pygame.display.flip()
	fpsClock.tick(FPS)
pygame.quit()
