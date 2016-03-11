import sys

zeefile = open(sys.argv[1], 'r')

def fib(number):
	if number == 0:
		return 0
	elif number == 1:
		return 1
	else:
		return fib(number - 1) + fib(number - 2)

for x in zeefile:
	holder = x.strip().split()

	num = int(holder[0])

	sys.stdout.write(str(fib(num)) + '\n')
