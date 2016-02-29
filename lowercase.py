import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	print x.strip().lower()
