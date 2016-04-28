from PIL import Image
import math
import sys
import random

from geoMath import *
from pointGenerators import *

C_RANGE = 255
MOD_RANGE = 256
WHITE = (255,255,255)
BLACK = (0,0,0)


#a point is a position/coordinate on the canvas
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def toString(self):
		return "Point("+str(self.x)+", "+str(self.y)+")"
	def addPoint(self, p):
		self.x = self.x+p.x
		self.y = self.y+p.y
	def addToPoint(self, p):
		return Point(self.x+p.x, self.y+p.y)
	def draw(self, canvas, colour=WHITE):
		try:
			canvas.pixels[self.x,self.y] = colour
		except IndexError:
			print(self.toString()+" out of range")
	def equals(self, p):
		return (self.x == p.x and self.y == p.y)

#a line is made up of two points, starting and end point
class Line():
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		self.points = self.lineToPoints()
	def diffX(self):
		return (self.p2.x - self.p1.x)
	def diffY(self):
		return (self.p2.y - self.p1.y)
	def draw(self, canvas, colour):
		for p in self.points:
			p.draw(canvas, colour)
	def diffPoints(self):
		return Vector(self.diffX(), self.diffY())
	def lineToPoints(self):
		dx, dy = self.diffX(), self.diffY()
		if dx == 0 and dy == 0:
			return [self.p1]
		elif dy == 0:
			return self.lineToPointsHorizontal()
		elif dx == 0:
			return self.lineToPointsVertical()
		else:
			if math.fabs(dx) == math.fabs(dy):
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
	def equals(self, l):
		if self.p1.equals(l.p1):
			if self.p2.equals(l.p2): return True
		if self.p1.equals(l.p2):
			if self.p2.equals(l.p1): return True
		return False
	def toString(self):
		return "Line("+self.p1.toString()+", "+self.p2.toString()+")"


#creates a square from two diagonal points 
class Rectangle():
	def __init__(self, p1, p2):
		self.p1, self.p2 = p1, p2
		self.points = (Point(p1.x,p1.y), Point(p1.x,p2.y), 
		               Point(p2.x,p2.y), Point(p2.x,p1.y))
		self.lines = (Line(self.points[0],self.points[1]),
					  Line(self.points[1],self.points[2]),
					  Line(self.points[2],self.points[3]),
					  Line(self.points[3],self.points[0]))
	def draw(self, canvas, colour):
		for line in self.lines:
			line.draw(canvas, colour)
	def fill(self, canvas, colour):
		for p in self.pointsOfArea():
			p.draw(canvas, colour)
	def isSquare(self):
		return (math.fabs(self.p1.x - self.p2.x) == math.fabs(self.p1.y - self.p2.y))
	def area(self):
		return int((math.fabs(self.p1.x-self.p2.x)+1)*(math.fabs(self.p1.y-self.p2.y)+1))
	def pointsOfArea(self):
		points = []
		dx = self.p2.x - self.p1.x
		dy = self.p2.y - self.p1.y
		for x in range(0, int(math.fabs(dx))+1):
			x = x*sign(dx)
			for y in range(0, int(math.fabs(dy))+1):
				y = y*sign(dy)
				points.append(Point(self.p1.x+x,self.p1.y+y))
		return points


#vector for position differences and moving and selections
class Vector(Point):
	def length(self):
		return math.sqrt(math.pow(self.x,2)+math.pow(self.y,2))

#a list of connected points
class Path():
	def __init__(self, points):
		self.points = points
		self.lines = self.makeLines()
	def makeLines(self):
		p = self.points
		if len(p) == 0 | 1:
			return []
		elif len(p) == 2:
			return [Line(p[0],p[1])]
		else:
			lines = []
			for i in range(0, len(p)-1):
				lines.append(Line(p[i],p[i+1]))
			return lines
	def draw(self, canvas, colour):
		for line in self.lines:
			line.draw(canvas, colour)
	def fill(self):
		p = self.points
	#def pointsOfArea(self):

	def isClosed(self):
		p = self.points
		return (p[0].equals(p[len(p-1)]))

#a visual bitmap drawing
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
		try:
			self.pixels[p.x,p.y] = colour
		except IndexError:
			print(p.toString()+" out of range")
	def drawLine(self, l, colour=WHITE):
		try:
			for p in l.points: self.pixels[p.x,p.y] = colour
		except  IndexError:
			print(p.toString()+"out of range")
	def saveToFile(self, file):
		self.image.save(file)

#defines a colour
class Colour():
	def __init__(self, r,g,b,a=C_RANGE):
		self.r = r%MOD_RANGE
		self.g = g%MOD_RANGE
		self.b = b%MOD_RANGE
		self.a = a
	def tuple(self):
		return (self.r,self.g,self.b,self.a)

class smoothColour():
	def __init__(self, r,g,b,a=C_RANGE):
		self.r = smoother(r)
		self.g = smoother(g)
		self.b = smoother(b)
		self.a = a
	def tuple(self):
		return (self.r,self.g,self.b,self.a)


#generates a line of points adding by a float
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
			
def pointGeneratorAdd(start,add):
	while True:
		yield start
		start = start.addToPoint(add)

def randomPoint(x,y):
	while True:
		yield Point(random.randint(x, y),random.randint(x, y))

def smoother(num):
	num = num%(C_RANGE*2)
	if num >= C_RANGE:
		num = C_RANGE*2-num
	return num

def bfs(point, canvas):
	p = canvas.pixels
	colour = p[point.x, point.y]
	allPoints = []
	done = []
	q = [('a',point)]
	directions = [('r',Point(1,0)),('u',Point(0,1)),('l',Point(-1,0)),('d',Point(0,-1))]

	x = 0
	while len(q) != 0:
		#print(x)
		curr = q.pop()
		x += 1
		print(curr[1].toString())
		for d in directions:
			passIt = False
			if d[0] == curr[0]: continue
			n = curr[1].addToPoint(d[1])
			for s in done:
				if s.equals(n):
					passIt = True
					break
			if passIt: 
				done.append(n)
				continue
			try:
				if p[n.x,n.y] == colour: 
					q.append((d[0], n))
				done.append(n)
			except IndexError:
				pass
		#if x == 5:
			#break
		allPoints.append(curr[1])
		done.append(curr[1])
	return allPoints





#gets all pixels around with the same colour
def fillPoints(point, canvas):
	p = canvas.pixels
	colour = p[point.x, point.y]
	v = Point(0,0)
	x = 0
	while x < 100:
		l = point.addToPoint(v)
		if p[l.x,l.y] == colour:
			print(p[x,y])
			print(l.toString())
		else: break
		x += 1




	'''
	for x in range(0, canvas.width):
		for y in range(0, canvas.height):
			if p[x,y] == colour: print(p[x,y])
	'''