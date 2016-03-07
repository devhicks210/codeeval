import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	holder = x.strip().split()

	print holder[-2]
