import sys
import re

zeefile = open(sys.argv[1])

for x in zeefile:
	holder = x.strip().split()

	letters = []

	nonrep = []

	for x in holder:
		for y in x:
			if x.count(y) == 1:
				nonrep.append(y)

	print nonrep[0]
