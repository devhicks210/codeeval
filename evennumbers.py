import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	nums = x.strip().split()

	for x in nums:
		x = int(x)

		if x % 2 == 0:
			print 1
		else:
			print 0
