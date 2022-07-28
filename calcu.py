
from gettext import translation
import pygame
pygame.init()


WINDOWWIDTH = 500
WINDOWHEIGHT = 650
WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTBLUE = (92,161,255)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
me1 = ' '
me2 = ' '
me3 = ' '
me4 = ' '
me5 = ' '
me6 = ' '
me7 = ' '
me8 = ' '
me9 = ' '
math_select = ' '
result_select = ' '
result = ' '


you_1 = ' '
you_2 = ' '





font = pygame.font.Font('freesansbold.ttf', 32)



screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('con cu lây tờ')
text = font.render('', True, green, blue)

num_1 = font.render('1', True, green, blue)
num_2 = font.render('2', True, green, blue)
num_3 = font.render('3', True, green, blue)

num_4 = font.render('4', True, green, blue)
num_5 = font.render('5', True, green, blue)
num_6 = font.render('6', True, green, blue)

num_7 = font.render('7', True, green, blue)
num_8 = font.render('8', True, green, blue)
num_9 = font.render('9', True, green, blue)

button1 = font.render('+', True, green, blue)
button2 = font.render('-', True, green, blue)
button3 = font.render('*', True, green, blue)
button4 = font.render('/', True, green, blue)
button5 = font.render('=', True, green, blue)

you_1 = ' '
you_2 = ' '






running = True

while running:
	screen.fill(LIGHTBLUE)
	mouse_x, mouse_y = pygame.mouse.get_pos()

	


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			#                            a   b   c    d

		cal_screen = pygame.draw.rect(screen, BLACK, (30, 30, 440, 90))#screen
		num_1_button = pygame.draw.rect(screen, BLACK, (30, 170 ,60, 70))#1
		num_4_button = pygame.draw.rect(screen, BLACK, (30, 300 ,60, 70))#4
		num_7_button = pygame.draw.rect(screen, BLACK, (30, 440 ,60, 70))#7

		num_2_button = pygame.draw.rect(screen, BLACK, (140, 170 ,60, 70))#2
		num_5_button = pygame.draw.rect(screen, BLACK, (140, 300 ,60, 70))#5
		num_8_button = pygame.draw.rect(screen, BLACK, (140, 440 ,60, 70))#8

		num_3_button = pygame.draw.rect(screen, BLACK, (250, 170 ,60, 70))#3
		num_6_button = pygame.draw.rect(screen, BLACK, (250, 300 ,60, 70))#6
		num_9_button = pygame.draw.rect(screen, BLACK, (250, 440 ,60, 70))#9

		plus_button = pygame.draw.rect(screen, BLACK, (380, 170, 90, 70))#+
		minus_button = pygame.draw.rect(screen, BLACK, (380, 300, 90, 70))#-
		times_button = pygame.draw.rect(screen, BLACK, (380, 440, 90, 70))#*
		degree_button = pygame.draw.rect(screen, BLACK, (380, 570, 90, 70))#/

		result_button = pygame.draw.rect(screen, BLACK, (30, 570, 280,70))#=

					#  mouse_x> a and mouse_x <= a+c:
					#   mouse_y >= b and mouse_y <= b+d

		
		# 1
		if mouse_x >= 30 and mouse_x <= 90 and mouse_y >= 170 and mouse_y <= 240 :
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('1')
				me1 = int(1)
		# 2
		elif mouse_x >= 140 and mouse_x <= 200 and  mouse_y >= 170 and mouse_y <= 240:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('2')
				me2 = int(2)
		# 3
		elif mouse_x >= 250 and mouse_x <= 310 and mouse_y >= 170 and mouse_y <= 240:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('3')
				me3 = int(3)
		# 4
		elif mouse_x >= 30 and mouse_x <= 90 and mouse_y >= 300 and mouse_y <= 370:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('4')
				me4 = int(4)
		# 5
		elif mouse_x >= 140 and mouse_x <= 200 and mouse_y >= 300 and mouse_y <= 370:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('5')
				me5 = int(5)
		# 6
		elif mouse_x >= 250 and mouse_x <= 310 and mouse_y >= 300 and mouse_y <= 370:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('6')
				me6 = int(6)
		# 7	
		elif mouse_x >= 30 and mouse_x <= 90 and mouse_y >= 440 and mouse_y <= 500:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('7')
				me7 = int(7)
		# 8
		elif mouse_x >= 140 and mouse_x <= 200 and mouse_y >= 440 and mouse_y <= 510:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('8')
				me8 = int(8)
		# 9
		elif mouse_x >= 250 and mouse_x <= 310 and mouse_y >= 440 and mouse_y <= 510:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('9')
				me9 = int(9)





		you_1 = str(me1) + str(me2) + str(me3) + str(me4) + str(me5) + str(me6) + str(me7) + str(me8) + str(me9) 
		text = font.render('{0}'.format(you_1) , True, green, blue)


		


		# +
		if mouse_x >= 380 and mouse_x <= 470 and mouse_y >= 170 and mouse_y <= 240:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('+')
				math_select = '+'
				text = font.render('+', True, green, blue)
		# -
		elif mouse_x >= 380 and mouse_x <= 470 and  mouse_y >= 300 and mouse_y <= 370:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('-')
				math_select = '-'
				text = font.render('-', True, green, blue)
		# *
		elif mouse_x >= 380 and mouse_x <= 470 and  mouse_y >= 440 and mouse_y <= 510:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('*')
				math_select = '*'
				text = font.render('*', True, green, blue)
		# /
		elif mouse_x >= 380 and mouse_x <= 470 and  mouse_y >= 570 and mouse_y <= 640:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('/')
				math_select = '/'
				text = font.render('/', True, green, blue)
		# =
		elif mouse_x >= 30 and mouse_x <= 310 and  mouse_y >= 570 and mouse_y <= 640:
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('=')
				result_select = '='
				text = font.render('=', True, green, blue)




		screen.blit(text, cal_screen)

		screen.blit(num_1, num_1_button)
		screen.blit(num_2, num_2_button)
		screen.blit(num_3, num_3_button)

		screen.blit(num_4, num_4_button)
		screen.blit(num_5, num_5_button)
		screen.blit(num_6, num_6_button)

		screen.blit(num_7, num_7_button)
		screen.blit(num_8, num_8_button)
		screen.blit(num_9, num_9_button)

		screen.blit(button1, plus_button)
		screen.blit(button2, minus_button)
		screen.blit(button3, times_button)
		screen.blit(button4, degree_button)

		screen.blit(button5, result_button)
		




 



















		# if math_select == '+' and result_select == '=':
		# 	result = you_1 + you_2
		# 	text = font.render(' {0} '.format(result), True, green, blue)
		# elif  math_select == '-' and result_select == '=':
		# 	result = you_1 - you_2
		# 	text = font.render(' {0} '.format(result), True, green, blue)
		# elif  math_select == '*' and result_select == '=': 
		# 	result = you_1 * you_2
		# 	text = font.render(' {0} '.format(result), True, green, blue)
		# elif  math_select == '/' and result_select == '=':
		# 	result = you_1 / you_2
		# 	text = font.render(' {0} '.format(result), True, green, blue)



		pygame.display.flip()
pygame.quit()

