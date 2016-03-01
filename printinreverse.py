import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	words = x.strip().split()

	mystring = ''

	for x in reversed(words):
		mystring = mystring + x + ' '

	print mystring[:-1]
