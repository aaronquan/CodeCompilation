from PIL import Image
import math
import sys

C_RANGE = 255
MOD_RANGE = 256
WHITE = (255,255,255)

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

class Point():
	def __init__(this, x, y):
		this.x = x
		this.y = y
	def toString(this):
		return "("+str(this.x)+","+str(this.y)+")"
	def addPoint(this, p):
		this.x = this.x+p.x
		this.y = this.y+p.y
	def addToPoint(this, p):
		return Point(this.x+p.x, this.y+p.y)
	def equals(this, p):
		return (this.x == p.x and this.y == p.y)

class Line():
	def __init__(this, p1, p2):
		this.p1 = p1
		this.p2 = p2
	def diffX(this):
		return (this.p1.x - this.p2.x)
	def diffY(this):
		return (this.p1.y - this.p2.y)
	def lineToPoints(this):
		dx = this.diffX()
		dy = this.diffY()
		points = []
		if dx == 0 and dy == 0:
			pass
		elif dy == 0:
			c = 0			
			while True:
				p = Point(this.p1.x, this.p1.y)
				p.addPoint(Point(c,0))
				points.append(p)
				if p.equals(this.p2): break
				c = convergeToByOne(c,-dx)
		elif dx == 0:
			c = 0
			while True:
				p = Point(this.p1.x, this.p1.y)
				p.addPoint(Point(0,c))
				points.append(p)
				if p.equals(this.p2): break
				c = convergeToByOne(c,-dy)
		else:
			print (dx > dy)
			if dx > dy:
				grad, cy = dy/dx, 0
				i = sign(grad)
				p = Point(this.p1.x, this.p1.y)
				points.append(p)
				while True:
					p = Point(this.p1.x, this.p1.y)
					print(p.toString())
					cy += grad
					if cy > 0.5: 
						p.addPoint(Point(-i,1))
						cy -= 1
					elif cy < -0.5: 
						p.addPoint(Point(-i,-1))
						cy += 1
					else: p.addPoint(Point(-i,0))
					points.append(p)
					if p.equals(this.p2): break
			if dx < dy:
				pass
			if dx == dy:
				pass
		return points

class Canvas():
	def __init__(this, width, height):
		this.width = width
		this.height = height
		this.image = Image.new("RGBA", (width, height))
		this.pixels = this.image.load()
	def background(this, colour):
		for x in range(this.width):
			for y in range(this.height):
				this.pixels[x,y] = colour
	def drawPoint(this, p, colour=WHITE):
		this.pixels[p.x,p.y] = colour
	def saveToFile(this, file):
		this.image.save(file)

class Colour():
	def __init__(this, r,g,b,a=C_RANGE):
		this.r = r%MOD_RANGE
		this.g = g%MOD_RANGE
		this.b = b%MOD_RANGE
		this.a = a
	def tuple(this):
		return (this.r,this.g,this.b,this.a)