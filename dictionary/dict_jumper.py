#!/bin/python

#first arg: a file containing all words
#second arg: a word (start)
#third arg: a word (end)

#this program creates the word ladder, 
#the shortest number of words it takes to transform one word to another changing one letter
#e.g. aim aid did dip hip hop 

import sys
import re, os

word_file = sys.argv[1]
start = sys.argv[2]
end = sys.argv[3]
wQueue = []
wBank = []
wordLadder = []
parent = {}
endWordDifference = {}
endL = False
wQueue.append(start)
parent[start]=None
end = end.lower()
endAsList = list(end)
temp = "tmp.txt"
t = open(temp, 'w')
#check end can have a word ladder
num = 0
f = open(word_file, 'r')
for line in f:
	line = line.rstrip()
	lower = line.lower()
	wordAsList=list(lower)
	diff = 0
	if len(wordAsList) != len(endAsList):
		continue
	t.write(line+'\n')
	for i in range(0, len(endAsList)):
		if wordAsList[i]!=endAsList[i]:
			diff = diff+1
	if diff == 1:
		num = num + 1
if num == 0:
	endL = True
f.close()

#create word ladder
while wQueue and not endL:
	curr = wQueue.pop(0)
	currLower = curr.lower()
	if curr == end:
		while parent[curr]!=None:
			wordLadder.insert(0, curr)
			curr = parent[curr]
		wordLadder.insert(0, start)
		break
	t = open(temp, 'r')
	for line in t:
		line = line.rstrip()
		lower = line.lower()
		wordAsList=list(lower)
		currAsList=list(currLower)
		if len(wordAsList) != len(currAsList):
			continue
		diff = 0
		for i in range(0, len(currAsList)):

			if wordAsList[i]!=currAsList[i]:
				diff = diff+1
		if diff == 1:
			if line not in wBank and line not in wQueue:

				parent[line]=curr
				diffEnd = 0
				for i in range(0, len(currAsList)):
					if endAsList[i]!=wordAsList[i]:
						diffEnd = diffEnd+1
				print line+": "+str(diffEnd)
				index = 0
				endWordDifference[line] = diffEnd
				for w in wQueue:
					if endWordDifference[w] > diffEnd:
						break
					index = index + 1
				wQueue.insert(index, line)
	wBank.append(curr)

for word in wordLadder:
	print word

if not wordLadder:
	print "No word ladder for "+start+" and "+end