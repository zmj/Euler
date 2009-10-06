from math import sqrt

def numPythTriples(perimeter):
	numTriples = 0
	for c in range(2, perimeter):
		for a in range(2, sqrt(c**2/2)):
			b = perimeter - c - a
			if a**2 + b**2 == c**2:
				#print str(a) + " " + str(b) + " " + str(c)
				numTriples += 1

	return numTriples

maxNumTriples = 0
maxNumPerimeter = 0
for p in range(10, 1001):
	num = numPythTriples(p)
	if num > maxNumTriples:
		maxNumTriples = num
		maxNumPerimeter = p

print maxNumPerimeter
