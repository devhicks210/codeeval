import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	holder = x.strip().split()

	mystring = []

	for x in holder:
		for y in x:
			if y.islower():
				if y == "a":
					mystring.append("0")
				elif y == "b":
					mystring.append("1")
				elif y == "c":
					mystring.append("2")
				elif y == "d":
					mystring.append("3")
				elif y == "e":
					mystring.append("4")
				elif y == "f":
					mystring.append("5")
				elif y == "g":
					mystring.append("6")
				elif y == "h":
					mystring.append("7")
				elif y == "i":
					mystring.append("8")
				elif y == "j":
					mystring.append("9")
				else:
					pass
			if y.isdigit():
					mystring.append(y)

	final = ''

	if mystring:
		for x in mystring:
			final = final + x
	else:
		final = final + "NONE"

	print final
