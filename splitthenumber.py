import sys

zeefile = open(sys.argv[1])

for x in zeefile:
	a, b = x.strip().split(" ")

	for x in b:
		if "-" in x:
			minloc = b.index(x)

			front = int(a[:minloc])
			back = a[minloc:].split()

			print front - int(back[0])
			
		if "+" in x:
			pluloc = b.index(x)

			front = int(a[:pluloc])
			back = a[pluloc:].split()

			print front + int(back[0])
