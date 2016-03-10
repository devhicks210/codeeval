import sys

zeefile = open(sys.argv[1], 'r')

for line in zeefile:
	holder = line.strip().split()

	mystring = ''

	for x in holder:
		size = len(x)

		mystring = mystring + str(x[size-1]) + str(x[1:size-1]) + str(x[0]) + ' '

	print mystring[:-1]
