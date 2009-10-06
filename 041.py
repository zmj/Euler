from zMath import nthLexiPerm
from zMath import isPrimeSimple
from zMath import factorial
import sys

for numDigits in range(9, 0, -1):
	sequence = range(1, numDigits+1)
	sequence.reverse()
	for permutationIndex in range(0, factorial(numDigits)):
		permutationStr = nthLexiPerm(sequence, permutationIndex)
		#print str(permutationIndex) + ": "+str(permutationStr)
		permutation = int(permutationStr)
		if isPrimeSimple(permutation):
			print permutation
			sys.exit(0)
