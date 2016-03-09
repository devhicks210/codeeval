import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	a, b = x.strip().split(',')

	if int(b) < int(a):
		count = 1
		while int(b) < int(a):

			if (int(b) * count) < int(a):
				count = count + 1
				continue
			else:
				print int(b) * count
				break
