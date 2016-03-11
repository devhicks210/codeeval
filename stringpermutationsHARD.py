
# h/t http://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python
import sys
from itertools import permutations

zeefile = open(sys.argv[1])

for x in zeefile:
	perm = list("".join(string) for string in permutations(x.strip()))

	mystring = ""

	for x in sorted(perm):
		mystring = mystring + x + ","

	print mystring[:-1]
