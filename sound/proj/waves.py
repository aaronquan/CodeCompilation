import sys
import math
import wave
import struct
import random
import argparse
from itertools import *

from PIL import Image

def main():
	sx, sy = 500, 500
	im = Image.new("RGB", (sx,sy), "black")
	pixels = im.load()
	sine = sine_wave(400.0)
	for i in range(sx):
		curr_sine = next(sine)
		print (math.floor(curr_sine*500))
		pixels[i,math.floor(curr_sine*500+250)] = (255,0,0) 
		for j in range(sy):
			if j == 250:
				pixels[i,j] = (255,255,255)
		print(curr_sine)


	im.save("image.png")

def sine_wave(frequency=440.0, framerate=44100, amplitude=0.5,
		skip_frame=0):
	'''
	Generate a sine wave at a given frequency of infinite length.
	'''
	if amplitude > 1.0: amplitude = 1.0
	if amplitude < 0.0: amplitude = 0.0
	for i in count(skip_frame):
		sine = math.sin(2.0 * math.pi * float(frequency) * (float(i) / float(framerate)))
		yield float(amplitude) * sine

main()