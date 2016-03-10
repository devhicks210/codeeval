import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	holder = x.strip().split()

	mystring = ''

	for x in holder:
		if not x[0].isdigit():
			mystring = mystring + x[0].upper() + x[1::] + " "
		else:
			mystring = mystring + x + " "

	print mystring[:-1]
