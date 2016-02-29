import sys

zeefile = open(sys.argv[1], 'r')

numbers = []

for x in zeefile:
	holder = x.strip().split()

	for x in holder:
		numbers.append(int(x))

print sum(numbers)
