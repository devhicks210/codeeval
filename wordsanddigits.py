import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	holder = x.strip().split()

	words = ''
	nums = ''

	for x in holder:
		items = x.split(',')

		for y in items:
			if y.isdigit() == True:
				nums = nums + y + ","
			else:
				words = words + y + ","

		if len(nums) == 0:
			print words[:-1]
		elif len(words) == 0:
			print nums[:-1]
		else:
			print words[:-1] + "|" + nums[:-1]
