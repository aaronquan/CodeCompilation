from PIL import Image
import math
import sys

white = (255,255,255)

def main():
	can = Canvas(400,400)
	im = Image.new("RGB", (can.width,can.height))
	pixels = im.load()
	p = Point(20,50)
	p.drawPoint(pixels)
	im.save("geometry.png")

class Point():
	def __init__(this, x, y):
		this.x = x
		this.y = y
	def toString(this):
		return "("+str(this.x)+","+str(this.y)+")"
	def addPoint(this, p):
		this.x = this.x+point.x
		this.y = this.x+point.y
	def drawPoint(this, pix):
		pix[this.x, this.y] = white

class Line():
	def __init__(this, p1, p2):
		this.p1 = p1
		this.p2 = p2

class Canvas():
	def __init__(this, width, height):
		this.width = width
		this.height = height

class Colour():
	def __init__(this, r, g, b):
		this.r = r%226
		this.g = r%226
		this.b = r%226
	def tuple():
		return (this.r,this.g,this.b)



main()