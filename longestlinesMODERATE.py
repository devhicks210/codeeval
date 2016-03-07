import sys

zeefile = open(sys.argv[1], 'r')

holder = []

for x in zeefile:
	holder.append(x.strip())

num = holder[0]
words = holder[1:]

mystring = ''

if words:
	words.sort(key = len)
	words.reverse()
	final = words[:int(num)]

	for x in final:
		print x
