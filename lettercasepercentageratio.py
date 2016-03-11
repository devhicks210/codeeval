import sys

zeefile = open(sys.argv[1], 'r')

def checklower(string):
	return sum(1 for c in string if c.islower())
def checkupper(string):
	return sum(1 for c in string if c.isupper())


for x in zeefile:
	holder = x.strip().split()

	for x in holder:
		lower = float(checklower(x)) * 100
		upper = float(checkupper(x)) * 100
		total = float(checklower(x)) + float(checkupper(x))

		if lower == 0:
			print "lowercase: 0.00 uppercase: 100.00"
		elif upper == 0:
			print "lowercase: 100.00 uppercase: 0.00"
		else:
			print "lowercase: %.2f uppercase: %.2f" % ((lower/total), (upper/total))
