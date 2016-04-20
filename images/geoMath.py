import math

def convergeToByOne(var, x):
	if var > x:
		var -= 1
	elif var < x:
		var += 1
	return var

def sign(var):
	if var > 0:
		return 1
	if var < 0:
		return -1
	return 0

def fabsCheck(p,q):
	return(math.fabs(p) > math.fabs(q))