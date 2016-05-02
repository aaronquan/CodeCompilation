from geometry import *
import itertools

def main():
	x,y = 400,400
	c = Canvas(x,y)
	black = Colour(0,0,0).tuple()
	white = Colour(255,255,255).tuple()
	green = Colour(0,255,0).tuple()
	red = Colour(255,0,0).tuple()
	blue = Colour(0,0,255).tuple()
	#c.background(black)

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
	'''
	#sq1 = Rectangle(Point(100,220), Point(240,80))
	#sq1.draw(c,blue)
	#sq1.fill(c,blue)
	#sq1.draw(c,green)
	'''
	'''
	sq2 = Rectangle(Point(70,40),Point(20,90))
	sq2.draw(c, blue)
	sq2pts = sq2.pointsOfArea()
	sq2.fill(c, green)
	pts = bfs(Point(50,50), c)
	print (len(pts))
	for p in pts:
		p.draw(c,red)
	'''
	'''
	q,w,e = Point(20,30), Point(60,20), Point(60,60)
	path = Path([q,w,e,q])
	path.draw(c, red)
	pts = bfs(Point(25,33), c)
	print (len(pts))
	for p in pts:
		p.draw(c,green)
	'''
	e = Point(int(x/2-1),int(y/2-1))
	cir = Circle(e, 20)
	cir.draw(c, green)
	print(len(cir.pointsOfArea()))
	print(len(fillPoints(e, c)))
	print(len(fillPoints(e, c)) == len(cir.pointsOfArea()))
	for p in cir.pointsOfArea():
		p.draw(c, red)
	c.saveToFile("geometry.png")
main()