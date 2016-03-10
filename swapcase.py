import sys

zeefile = open(sys.argv[1], 'r')


for line in zeefile:
	holder = line.strip().split()

	mystring = ''

	for x in holder:
		mystring = mystring + x.swapcase() + " "

	print mystring[:-1]
