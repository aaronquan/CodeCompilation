from geometry import *
#from pointGenerators import *

def main():
	c = Canvas(400,400)
	black = Colour(0,0,0).tuple()
	white = Colour(255,255,255).tuple()
	green = Colour(0,255,0).tuple()
	red = Colour(255,0,0).tuple()
	blue = Colour(0,0,255).tuple()
	c.background(black)

	e,f,g = Point(60,50), Point(10,90), Point(100,120)
	h,i,j = Point(200,200), Point(350,100), Point(150,330)

	l1 = Line(e,f)
	l2 = Line(f,g)
	l3 = Line(e,g)

	triangle = [Line(h,i),Line(i,j),Line(j,h)]
	for line in triangle:
		for point in line.points:
			c.drawPoint(point, green)
	for point in l1.points:
		c.drawPoint(point,white)
	for point in l2.points:
		c.drawPoint(point, red)
	for point in l3.points:
		c.drawPoint(point, blue)
	
	c.saveToFile("geometry.png")
main()