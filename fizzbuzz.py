import sys

zeefile= open(sys.argv[1], 'r')

for x in zeefile:
	a, b, c = x.strip().split()

	printthis = ''

	for x in range(1, int(c) + 1):
		if x % int(a) == 0 and x % int(b) == 0:
			printthis = printthis + "FB "
		elif x % int(a) == 0:
			printthis = printthis + "F "
		elif x % int(b) == 0:
			printthis = printthis + "B "
		else:
			printthis = printthis + str(x) + " "

	print printthis[:-1]
