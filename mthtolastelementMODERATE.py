import sys

zeefile = open(sys.argv[1], 'r')

for x in zeefile:
	holder = x.strip().split(" ")

	num = holder[-1]

	holder.reverse()

	newlist = holder[1:]

	if int(num) <= len(newlist):
		
		sys.stdout.write(newlist[int(num)-1] + '\n')
	
	else:
		pass
