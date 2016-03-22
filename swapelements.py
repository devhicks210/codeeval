import sys

zeefile = open(sys.argv[1])

for x in zeefile:
	holder = x.strip().split(" : ")

	a = holder[0].split()
	b = holder[1].split(', ')

	mystring = ''

	for x in b:
		uno, dos = x.split('-')

		uno = int(uno)
		dos = int(dos)

		a[uno], a[dos] = a[dos], a[uno]

	for x in a:
		mystring = mystring + x + " "

	print mystring[:-1]
