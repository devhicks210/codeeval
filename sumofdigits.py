zeefile = open('sumofdigits.txt')

for x in zeefile:
	holder = x.strip().split()

	numbers = []

	for y in holder:
		for z in y:
			numbers.append(int(z))

	print sum(numbers)
