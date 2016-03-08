import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	a = x.strip().split(";")

	b = a[1].split(",")

	c = []

	for x in b:
		if x not in c:
			c.append(x)
		else:
			print x
