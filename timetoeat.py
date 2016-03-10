import sys

zeefile = open(sys.argv[1], 'r')

for line in zeefile:
	holder = line.strip().split()

	holder.sort()

	holder.reverse()

	mystring = ''

	for x in holder:
		mystring = mystring + x + " "

	print mystring[:-1]
