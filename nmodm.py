import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	a, b = x.strip().split(",")

	a = int(a)
	b = int(b)

	uno = a / b
	
	dos = b * uno

	tres = a - dos

	print tres
