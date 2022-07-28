
from random import randint
print('------')

running = True

while running:
	print('------')
	me = input('ban chon: ')
	bot = randint(0,1)


	if bot == 0:
		bot = 'dam'
	if bot == 1:
		bot = 'la'
	if bot == 2:
		bot = 'keo'
	print('bot chon: ',bot)



	print('-------')

	if me == bot:
		print('draw')
	elif me == 'stop':
		running = False
	else:
		
		if me =='dam':
			if bot =='la':
				print('bot win')
			else:
				print('you win')
		elif me =='la':
			if bot == 'dam':
				print('you win')
			else:
				print('bot win')
		elif me =='keo':
			if bot=='dam':
				print('bot win')
			else:
				print('you win')
		else:
			print('nhap saiiii!')


 