def getNext(n):
	if n % 2 == 0:
		return n/2
	else:
		return 3*n + 1

def doSequence(x):
	sequence = list()
	sequence.append(x)
	while x != 1:
		x = getNext(x)
		sequence.append(x)
	return sequence

longestSequence = 0
num = 0
for i in range(1,1000000):
	seqLength = len(doSequence(i))
	if seqLength > longestSequence:
		longestSequence = seqLength
		num = i

print num
