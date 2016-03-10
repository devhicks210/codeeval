import sys

zeefile = open(sys.argv[1], 'r')

for line in zeefile:
	holder = line.strip().split('| ')

	letts = []
	nums = []

	mystring = ''

	if holder[0] != '':
		for x in holder[0]:
			letts.append(x)

		nums.append(holder[1].split(' '))

		for x in nums:
			for y in x:
				mystring = mystring + holder[0][int(y) - 1]

		print mystring
