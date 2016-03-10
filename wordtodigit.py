import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	holder = x.strip().split(';')

	mystring = ''

	for x in holder:
		if x == "zero":
			mystring = mystring + "0"
		if x == "one":
			mystring = mystring + "1"
		if x == "two":
			mystring = mystring + "2"
		if x == "three":
			mystring = mystring + "3"
		if x == "four":
			mystring = mystring + "4"
		if x == "five":
			mystring = mystring + "5"
		if x == "six":
			mystring = mystring + "6"
		if x == "seven":
			mystring = mystring + "7"
		if x == "eight":
			mystring = mystring + "8"
		if x == "nine":
			mystring = mystring + "9"

	print mystring
