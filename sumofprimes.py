# Yes. I totally cheated.

nums = []

for p in range(2, 7920):
	for i in range(2, p):
		if p % i == 0:
			break
	else:
		nums.append(p)

print sum(nums)
