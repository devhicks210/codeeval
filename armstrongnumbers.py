import sys

zeefile = open(sys.argv[1])

for x in zeefile:
	holder = x.strip().split()

	indienums = holder[0]

	totalnums = []

	for x in indienums:
		x = int(x)
		totalnums.append(x ** len(indienums))

	if str(sum(totalnums)) == indienums:
		print "True"
	else:
		print "False"
