import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	a = x.strip().split()

	for x in a:
		print int(x, 16)
