import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	holder = x.strip().split()

	nums = []

	for x in holder:
		if holder.count(x) == 1:
			nums.append(x)
		else:
			pass

	if nums:
		nums.sort()
		mykey = nums[0]
		print holder.index(mykey) + 1
	else:
		print 0
