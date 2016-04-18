from geometry import *

def main():
	c = Canvas(400,400)

	white = Colour(255,255,255).tuple()
	green = Colour(0,255,0).tuple()
	red = Colour(255,0,0).tuple()

	p,q = Point(20,50), Point(10,50)
	a,s = Point(100,120), Point(100,50)

	c.background(green)

	l1 = Line(p,q)
	l2 = Line(a,s)
	#l3 = Line(a,q)
	linePoints1 = l1.lineToPoints()
	linePoints2 = l2.lineToPoints()
	#linePoints3 = l3.lineToPoints()
	#print (linePoints3)
	for point in linePoints1:
		c.drawPoint(point.addToPoint(Point(0,1)),white)
		c.drawPoint(point.addToPoint(Point(0,-1)),white)
		c.drawPoint(point,white)

	for point in linePoints2:
		c.drawPoint(point, red)
		c.drawPoint(point.addToPoint(Point(-1,0)), red)

	c.saveToFile("geometry.png")
main()