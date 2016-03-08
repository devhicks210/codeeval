import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	holder = x.strip().split()

	for x in holder:
		x = int(x)
		print bin(x)[2:]
