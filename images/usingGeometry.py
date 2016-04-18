from geometry import *

def main():
	c = Canvas(400,400)
	p,q = Point(20,50), Point(10,50)
	l = Line(p,q)
	white = Colour(255,255,255).tuple()
	c.drawPoint(p, white)
	linePoints = l.lineToPoints()
	for point in linePoints:
		#print(point.toString())
		c.drawPoint(point.addToPoint(Point(0,1)),white)
		c.drawPoint(point.addToPoint(Point(0,-1)),white)
		c.drawPoint(point,white)
	c.saveToFile("geometry.png")
main()