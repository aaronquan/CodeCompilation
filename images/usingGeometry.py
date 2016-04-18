from geometry import *

def main():
	c = Canvas(400,400)
	white = Colour(255,255,255).tuple()
	green = Colour(0,255,0).tuple()
	p,q = Point(20,50), Point(10,50)
	c.background(green)
	l = Line(p,q)
	c.drawPoint(p, white)
	linePoints = l.lineToPoints()
	for point in linePoints:
		#print(point.toString())
		c.drawPoint(point.addToPoint(Point(0,1)),white)
		c.drawPoint(point.addToPoint(Point(0,-1)),white)
		c.drawPoint(point,white)
	c.saveToFile("geometry.png")
main()