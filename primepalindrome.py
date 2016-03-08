nums = ''

for p in range(2, 1000):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        nums = nums + str(p) + ","


holder = nums.split(',')

final = []

for x in holder:
	if x > 1:
		if x == x[::-1]:
			final.append(x)

print final[-2]
