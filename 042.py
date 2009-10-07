letterScores = dict()
for i in range(1, 27):
	letterScores[ chr( 64 + i) ] = i

def wordScore(word):
	score = 0
	for c in word:
		score += letterScores[c]
	return score

file = open("words.txt")
text = file.read()
words = text.split(",")
for i in range(0, len(words)):
	words[i] = words[i][1:-1]

triangleNums = [ 1 ]
def isTriangleNumber(num):
	if num > triangleNums[-1]:
		n = len(triangleNums)
		while True:
			nextTriangleNum = (n*(n+1))/2
			triangleNums.append(nextTriangleNum)
			if nextTriangleNum > num:
				break
			else:
				n += 1

	return num in triangleNums

numTriangleWords = 0
for word in words:
	if isTriangleNumber(wordScore(word)):
		numTriangleWords += 1
print numTriangleWords
