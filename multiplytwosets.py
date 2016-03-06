import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	holder = x.strip().split()

	bar = holder.index("|")

	mystring = ''

	a = holder[0:bar]
	b = holder[bar+1:]

	for y, z in zip(a, b):
		mystring = mystring +  str(int(y) * int(z)) + " "

	print mystring[:-1]
