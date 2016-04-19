import itertools
from geometry import *

def numbers(i):
	n = i
	while True:
		yield n
		n += 1

def adjPointGen(i,j):
	a,b = (0,0)
	while True:
		yield Point(a,b)
		a += i
		b += j
