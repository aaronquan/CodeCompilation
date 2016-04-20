import itertools

def numbers(i):
	n = i
	while True:
		yield n
		n += 1

def pointGeneratorAdd(start,add):
	while True:
		yield start
		start = start.addToPoint(add)
