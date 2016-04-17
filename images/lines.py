#lines.py

from PIL import Image
import math
import sys

def main():
	sx, sy = 500, 500
	im = Image.new("RGB", (sx,sy), "black")
	pixels = im.load()
	q,w = point(20, 40), point(80, 30)
	points = line(q,w)
	im = drawLine(points, im)
	im.save("lines.png")

def point(x, y):
	return [x,y]

def line(p1, p2):
	points = []
	dx = p1[0] - p2[0]
	dy = p1[1] - p2[1]
	while p1[0] < p2[0]:
		points.append((p1[0],p1[1]))
		p1[0] += math.floor(-dx/dy)
		p1[1] += 1
	points.append((p2[0], p2[1]))
	return points

def drawLine(points, im):
	pixels = im.load()
	for p in points:
		pixels[p[0],p[1]] = (0,255,255)
	return im
main()