from geometry import *

def main():
	c = Canvas(400,400)
	black = Colour(0,0,0).tuple()
	white = Colour(255,255,255).tuple()
	green = Colour(0,255,0).tuple()
	red = Colour(255,0,0).tuple()
	blue = Colour(0,0,255).tuple()

	a,p,s = Point(60,50), Point(10,90), Point(100,120)
	q,w,e = Point(200,200), Point(350,100), Point(150,330)

	c.background(black)

	l1 = Line(a,p)
	l2 = Line(p,s)
	l3 = Line(s,a)

	#triangle = [Line(q,w),Line(w,e),Line(e,q)]
	for point in Line(q,w).points:
		c.drawPoint(point, green)

	for point in l1.points:
		#c.drawPoint(point.addToPoint(Point(0,1)),white)
		#c.drawPoint(point.addToPoint(Point(0,-1)),white)
		c.drawPoint(point,white)
	for point in l2.points:
		c.drawPoint(point, red)
		#c.drawPoint(point.addToPoint(Point(-1,0)), red)
	for point in l3.points:
		c.drawPoint(point, blue)

	c.saveToFile("geometry.png")
main()