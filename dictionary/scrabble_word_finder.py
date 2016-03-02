#scrabble word finder
import sys

def scoreLetters():
	score = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
			'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
			'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
			's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
			'y': 4, 'z': 8}
	return score

def wordScore(word, scoring):
	letters = list(word)
	score = 0
	for l in letters:
		score = score + scoring[l]
	return score
#returns a bool
def letInList(let, lList):
	boo = False
	for l in lList:
		if let == l:
			boo = True
			break
	return boo

#l: list of letters
#wFile: the file to find words from
def getWords(letterList, wFile):
	scoring = scoreLetters()
	wordList = []
	scoreWord = {}
	maxLetters = len(letterList)
	f = open(wFile, 'r')
	for line in f:
		line = line.rstrip()
		wordAsList = list(line)
		wordLen = len(wordAsList)
		if wordLen > maxLetters or wordLen <= 1:
			continue
		newLetterList = list(letterList)
		count = 0
		for let in wordAsList:
			if letInList(let, newLetterList):
				newLetterList.remove(let)
				count = count + 1
		#print "word: "+line+"  found: "+str(count)+":"+str(len(wordAsList))
		if count == wordLen:
			score = wordScore(line, scoring)
			index = 0
			for w in wordList:
				if score < scoreWord[w]:
					break
				index = index + 1
			scoreWord[line] = score
			wordList.insert(index, line)
	return wordList

def main():
	wFile = sys.argv[1]
	letters = sys.argv[2]
	try:
		cond = sys.argv[3]
	except:
		pass

	letters = list(letters)
	scoring = scoreLetters()
	words = getWords(letters, wFile)

	for word in words:
		score = wordScore(word, scoring)
		print word+': '+str(score)
	return
main()