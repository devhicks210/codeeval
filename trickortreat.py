import sys

zeefile = open(sys.argv[1], 'r')

vampire = 3
zombie = 4
witch = 5

for x in zeefile:
	v, z, w, h = x.strip().split(',')

	vamp = v.split(": ")
	zomb = z.split(": ")
	wit = w.split(": ")
	house = h.split(": ")

	tvamp = int(vamp[1])
	tzomb = int(zomb[1])
	twit = int(wit[1])
	thouse = int(house[1])
	tkids = tvamp + tzomb + twit

	print ((tvamp * vampire) + (tzomb * zombie) + (twit * witch)) * thouse / tkids
