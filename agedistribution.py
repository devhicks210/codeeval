import sys

zeefile = open(sys.argv[1])

for x in zeefile:
	x = x.strip().split()

	for n in x:

		n = int(n)
		if n < 0:
			print "This program is for humans"
		if n in range(0, 3):
			print "Still in Mama's arms"
		if n in range(3, 5):
			print "Preschool Maniac"
		if n in range(5, 12):
			print "Elementary school"
		if n in range(12, 15):
			print "Middle school"
		if n in range(15, 19):
			print "High school"
		if n in range(19, 23):
			print "College"
		if n in range(23, 66):
			print "Working for the man"
		if n in range(66, 101):
			print "The Golden Years"
		if n > 100:
			print "This program is for humans"
