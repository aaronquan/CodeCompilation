from PIL import Image
import math
import sys

from geoMath import *
from pointGenerators import *

C_RANGE = 255
MOD_RANGE = 256
WHITE = (255,255,255)
BLACK = (0,0,0)

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def toString(self):
		return "("+str(self.x)+","+str(self.y)+")"
	def addPoint(self, p):
		self.x = self.x+p.x
		self.y = self.y+p.y
	def addToPoint(self, p):
		return Point(self.x+p.x, self.y+p.y)
	def equals(self, p):
		return (self.x == p.x and self.y == p.y)

class Line():
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		self.points = self.lineToPoints()
	def diffX(self):
		return (self.p2.x - self.p1.x)
	def diffY(self):
		return (self.p2.y - self.p1.y)
	def lineToPoints(self):
		dx = self.diffX()
		dy = self.diffY()
		i,j = sign(dx),sign(dy)
		p = Point(self.p1.x, self.p1.y)
		points = [p]
		if dx == 0 and dy == 0:
			return [self.p1]
		elif dy == 0:
			return self.lineToPointsHorizontal()
		elif dx == 0:
			return self.lineToPointsVertical()
		else:
			if math.fabs(dx) == math.fabs(dy):
				#return self.lineToPointsDiagonal()
				return self.lineToPointsPerfectDiagonal()
			else:
				return self.lineToPointsDiagonal()
		return points
	def lineToPointsHorizontal(self):
		points = []
		gen = pointGeneratorAdd(self.p1, Point(sign(self.diffX()), 0))
		while True:
			p = next(gen)
			points.append(p)
			if p.x == self.p2.x: break
		return points
	def lineToPointsVertical(self):
		points = []
		gen = pointGeneratorAdd(self.p1, Point(0, sign(self.diffY())))
		while True:
			p = next(gen)
			points.append(p)
			if p.y == self.p2.y: break
		return points
	def lineToPointsPerfectDiagonal(self):
		points = []
		gen = pointGeneratorAdd(self.p1, Point(sign(self.diffX()), sign(self.diffY())))
		while True:
			p = next(gen)
			points.append(p)
			if p.y == self.p2.y and p.x == self.p2.x: break
		return points
	def lineToPointsDiagonal(self):
		points = []
		gen = pointGeneratorFloat(self.p1, self.diffX(), self.diffY())
		while True:
			p = next(gen)
			points.append(p)
			if p.equals(self.p2): break
		return points

class Canvas():
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.image = Image.new("RGBA", (width, height))
		self.pixels = self.image.load()
	def background(self, colour):
		for x in range(self.width):
			for y in range(self.height):
				self.pixels[x,y] = colour
	def drawPoint(self, p, colour=WHITE):
		self.pixels[p.x,p.y] = colour
	def saveToFile(self, file):
		self.image.save(file)

class Colour():
	def __init__(self, r,g,b,a=C_RANGE):
		self.r = r%MOD_RANGE
		self.g = g%MOD_RANGE
		self.b = b%MOD_RANGE
		self.a = a
	def tuple(self):
		return (self.r,self.g,self.b,self.a)

def pointGeneratorFloat(start, xf, yf):
	c = 0
	if fabsCheck(xf,yf):
		grad = math.fabs(yf/xf)
		while True:
			yield start
			c += grad*sign(yf)
			if c > 0.5:
				start = start.addToPoint(Point(sign(xf),1))
				c -= 1
			elif c < -0.5:
				start = start.addToPoint(Point(sign(xf),-1))
				c += 1
			else:
				start = start.addToPoint(Point(sign(xf),0))
	elif fabsCheck(yf,xf):
		grad = math.fabs(xf/yf)
		while True:
			yield start
			c += grad*sign(xf)
			if c > 0.5:
				start = start.addToPoint(Point(1,sign(yf)))
				c -= 1
			elif c < -0.5:
				start = start.addToPoint(Point(-1,sign(yf)))
				c += 1
			else:
				start = start.addToPoint(Point(0,sign(yf)))
	else:
		gen = pointGeneratorAdd(start, Point(sign(xf), sign(yf)))
		while True:
			yield next(gen)