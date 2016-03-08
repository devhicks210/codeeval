import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	a, b = x.strip().split(',')

	top = int(b)
	bottom = int(a)

	mystring = ''

	nums = []

	for p in range(2, 1000):
	    for i in range(2, p):
	        if p % i == 0:
	            break
	    else:
	        if p >= bottom and p <= top:
	        	nums.append(p)
	        	
	print len(nums)
