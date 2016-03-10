import sys

zeefile = open(sys.argv[1], 'r')

for line in zeefile:
	holder = line.strip().split()

	print max(holder, key = len)
