from zMath import numericPermutations
from zMath import PrimeGen
import sets


primegen = PrimeGen(10000)

primes = list()
for p in range(1001, 10001, 2):
	if primegen.isPrimeHash(p):
		primes.append(p)

permutationGroups = dict()
for num in primes:
	numSet = frozenset(str(num))
	if numSet not in permutationGroups:
		permutationGroups[numSet] = list()
	permutationGroups[numSet].append(num)

for numSet, numList in permutationGroups.items():
	if len(numList) < 3:
		del permutationGroups[numSet]


for numList in permutationGroups.itervalues():
	#print numList
	for i in range(0, len(numList)-2):
		for j in range(i+1, len(numList)-1):
			num1 = numList[i]
			num2 = numList[j]
			num3 = num2 - (num1 - num2)
			if num3 in numList:
				print str(num1), str(num2), str(num3)

