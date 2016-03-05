import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	holder = x.strip().split(',')

	nums = []

	mystring = ''

	for num in holder:
		if num not in nums:
			nums.append(num)

	for x in nums:
		mystring = mystring + x + ','

	print mystring[:-1]
