import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	holder = x.strip().split()

	numbers = []

	for y in holder:
		for z in y:
			numbers.append(int(z))

	print sum(numbers)
