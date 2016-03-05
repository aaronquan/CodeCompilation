#!/bin/python
from __future__ import division
import Image
import math
import sys

cr = 255

def main():
	#cr = 255
	sx=int(sys.argv[1])
	sy=int(sys.argv[2])
	#sx = 256
	#sy = 256
	im = Image.new("RGB", (sx,sy), "black")
	pixels = im.load()

	mulx = cr/sx
	muly = cr/sy

	for i in range(sx):
		for j in range(sy):
			x = i-sx/2
			y = -(j-sy/2)

			r = x*mulx
			g = y*muly
			b = math.fabs(y)*mulx+math.fabs(x)*mulx
			r,g,b =colourPublish(r, g, b)

			#for i1 in range(int(-sx/2),int(sx/2)+10, 10):
			#	r,g,b = lineGradient(x,y, 1, 1, i1, 0, 2, cr, cr/2, 0, r, g, b, strn=cr/2)
			#	r,g,b = lineGradient(x,y, 1, -1, i1, 0, 2, 0, cr/2, cr, r, g, b, strn=cr/2)

			r,g,b = colourPublish(r, g, b)

			#printArea(x,y, 5, 5, r, g, b)
			pixels[i,j] = (r, g, b)
			
	#im.show()
	im.save("image.bmp")

def colourPublish(r, g, b):
	r = int(math.fabs(r))
	g = int(math.fabs(g))
	b = int(math.fabs(b))
	r = smoother(r)
	g = smoother(g)
	b = smoother(b)
	return r, g, b
def smoother(num):
	cr = 255
	num = num%(cr*2)
	if num >= cr:
		num = cr*2-num
	return num

#line tool with gradient and point
#gradient of line: grx/gry
#colour of line: colr, colg, colb
#line width: wid
#colour strength: strn
#spx, spy: starting position of line
#len: length of the line

#usage: (x,y, a1,a2, c1,c2,c3, x1,y1, l, w, r, g, b, s)
#x,y, r,g,b not user inputted
def lineGradient(x, y, grx, gry, spx, spy, wid, colr, colg, colb, r, g, b, strn=cr):
	wMod = math.fabs(grx)+math.fabs(gry)
	sp = grx*spx - gry*spy
	l = grx*x - gry*y - sp
	#if spx == x and spy == y:
	#	return 0, 0, 0
	if l <= (wid-1)*wMod and l >= -(wid-1)*wMod:
		if strn/cr == 1:
			lr, lg, lb = colr, colg, colb
		else:
			lr, lg, lb = colourMix(colr, colg, colb, r, g, b, strn)
	else:
		lr, lg, lb = r, g, b
	return lr, lg, lb

#line point to point

def linePoint(x, y, px1, py1, px2, py2, wid, colr, colg, colb, r, g, b, strn=cr):
	return r, g, b

#base colour: r, g, b
#colour added to base: colr, colg, colb
#intensity of the colour adding: strn
def colourMix(colr, colg, colb, r, g, b, strn):
	strnR = strn/cr
	r,g,b = colourPublish(r, g, b)
	colr,colg,colb = colourPublish(colr, colg, colb)
	dr, dg, db = colr - r, colg - g, colb - b
	return r+dr*strnR, g+dg*strnR, b+db*strnR

#prints the square from the centre
def printArea(x,y, h, w, r, g, b):
	if x < w and x > -w and y < h and y > -w:
		print "x: "+str(x)+" y: "+str(y)+" value: "+str(r)+" "+str(g)+" "+str(b)
#gradient of line: grx/gry
#colour of line: colr, colg, colb
#line width: wid
def lineOld(x, y, grx, gry, colr, colg, colb, wid, r, g, b):
	l = grx*x - gry*y
	if l <= wid and l >= -wid:
		lr, lg, lb = colr, colg, colb
	else:
		lr, lg, lb = r, g, b
	return lr, lg, lb

#a1, a2, a3, a4, a5, a6, a7, a8 = p1(x,y)

#r = 5*(a1 + a4 + a7 + a2)
#g = 5*(a2 + a8 + a3 + a1)
#b = 5*(a3 + a6 + a1 + a4)
def p1(x,y):
	ud = ((x**2+y**2)/(x**2+1))
	uurddl = ((x**2+y**2)/((2*x+y)**2+1))
	urdl = ((x**2+y**2)/((x+y)**2+1))
	urrdll = ((x**2+y**2)/(x**2+1))
	rl = ((x**2+y**2)/(y**2+1))
	ulldrr = ((x**2+y**2)/((x-2*y)**2+1))
	uldr = ((x**2+y**2)/((x-y)**2+1))
	uulddr = ((x**2+y**2)/((2*x-y)**2+1))
	return ud, uurddl, urdl, urrdll, rl, ulldrr, uldr, uulddr

main()