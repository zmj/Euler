from zMath import nthLexiPerm
from zMath import factorial

def hasWeirdProperty(n): #10 digit number
	s = str(n)
	if s[0] == '0':
		return False

	return int(s[1:4]) % 2 == 0 and int(s[2:5]) % 3 == 0 and int(s[3:6]) % 5 == 0 and int(s[4:7]) % 7 == 0 and int(s[5:8]) % 11 == 0 and int(s[6:9]) % 13 == 0 and int(s[7:10]) % 17 == 0


sum = 0
sequence = range(0, 10)
#should probably write a permutation generator instead of using this function
for permutationIndex in range(0, factorial(10)):
	permutation = nthLexiPerm(sequence, permutationIndex)
	if hasWeirdProperty(permutation):
		sum += int(permutation)

print sum
