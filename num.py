import random
r = random.randint(1,100)
while True:
	num = input('Please enter a number: ')
	num = int(num)
	if num == r:
			print('You win')
			break
	elif num > r:
			print('Your number is Bigger')
	elif num < r:
			print('Your number is Smaller')
