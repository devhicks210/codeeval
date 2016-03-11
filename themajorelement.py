import sys

zeefile = open(sys.argv[1])

for x in zeefile:
	holder = x.strip().split(",")

	tot = len(holder)

	uniques = []

	final = []

	for x in holder:
		if x not in uniques:
			uniques.append(x)

	for x in uniques:
		if holder.count(x) > (tot/2):
			final.append(int(x))

	if not final:
		print "None"
	else:
		for x in final:
			print x
