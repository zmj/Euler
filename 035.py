from zMath import PrimeGen

primesBelow = 1000000

primes = PrimeGen(primesBelow)


def isCircularPrime(n):
	numStr = str(n)
	numLength = len(numStr)
	for i in range(0, numLength):
		subStr1 = numStr[0:i]
		subStr2 = numStr[i:numLength]
		newNum = int(subStr2 + subStr1)
		if not primes.isPrime(newNum):
			return False
	return True


numPrimes = 0
for p in range(2, primesBelow):
	if isCircularPrime(p):
		#print p
		numPrimes += 1

print numPrimes
