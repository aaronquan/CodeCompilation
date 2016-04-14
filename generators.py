#learning generators in python
from itertools import *

def main():
	'''
	f = nFibonacci(10)
	print(list(f))
	print(list(firstn(fibonacci(), 10)))
	
	l = ['6','4','a']
	print(list(permutations(l)))
	'''
	for time in trange((10, 10, 10), (13, 50, 15), (0, 15, 12) ):
		print(time)

def trange(start, end, inc):
	curr = list(start)
	end = list(end)
	while curr < end:
		yield tuple(curr)
		curr = [sum(x) for x in zip(curr, inc)]
		for x in range(1,3):
			if curr[x] > 60:
				curr[x] = curr[x] - 60
				curr[x-1] += 1

def firstn(g, n):
	for i in range(n):
		yield next(g)
#fibonacci example

def nFibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter >= n): 
            return
        yield a
        a, b = b, a + b
        counter += 1

def fibonacci():
	a, b = 0, 1
	while True:
		yield a
		a,b = b, a+b

def permutations(items):
	n = len(items)
	if n==0: yield []
	else:
		for i in range(len(items)):
			for cc in permutations(items[:i]+items[i+1:]):
				yield [items[i]]+cc


main()