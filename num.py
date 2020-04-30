import random
start = input('Please input Start number: ')
end = input('Please input End number: ')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
	count += 1 #count = count + 1
	num = input('Please enter a number: ')
	num = int(num)
	if num == r:
			print('You win')
			break
	elif num > r:
			print('Your number is Bigger')
	elif num < r:
			print('Your number is Smaller')

	print('This is your ', count, ' time')
