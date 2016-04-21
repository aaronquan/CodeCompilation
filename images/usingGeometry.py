from geometry import *
import itertools

def main():
	x,y = 600,600
	c = Canvas(x,y)
	black = Colour(0,0,0).tuple()
	white = Colour(255,255,255).tuple()
	green = Colour(0,255,0).tuple()
	red = Colour(255,0,0).tuple()
	blue = Colour(0,0,255).tuple()
	c.background(black)

	'''
	p_array = []
	gen = randomPoint(0, x-1)
	for n in range(0,20):
		p_array.append(next(gen))
	comb = itertools.combinations(p_array, 2)
	x = 0
	for points in comb:
		l = Line(points[0],points[1])
		for point in l.points:
			x += 1
			c.drawPoint(point, smoothColour(x*2,x*3,x).tuple())
	'''
	'''
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
	'''

	sq1 = [Point(100,80), Point(100,220), Point(240,220), Point(240,80)]
	lines = []
	x = 0
	while x < len(sq1)-1:
		l = lines.append(Line(sq1[x], sq1[x+1]))
		x += 1
	lines.append(Line(sq1[len(sq1)-1], sq1[0]))
	for l in lines:
		print(l.toString())
		for pt in l.points:
			c.drawPoint(pt, red)

	sq2 = Square(Point(100,80+200),Point(240,220+200))
	for l in sq2.lines:
		print(l.toString())
		for pt in l.points:
			c.drawPoint(pt, green)

	c.saveToFile("geometry.png")
main()