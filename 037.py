from zMath import PrimeGen

primes = PrimeGen(1000000)
print "primes generated"

class TruncateDirection:
	LEFT = 1
	RIGHT = 2

def isTruncatedPrime(n, direction):
	numStr = str(n)

	leftMod = 0
	if direction == TruncateDirection.LEFT:
		leftMod = 1
	rightMod = len(numStr)
	if direction == TruncateDirection.RIGHT:
		rightMod = -1
	
	while len(numStr) > 0:
		p = int(numStr)
		#print "Checking: "+numStr
		if not primes.isPrime(p):
			return False
		numStr = numStr[leftMod:rightMod]

	return True

primeCount = 0
sum = 0

primeIndex = 0
while primeCount < 11:
	p = primes.primes[primeIndex]
	if p < 10:
		primeIndex += 1
		continue

	if isTruncatedPrime(p, TruncateDirection.LEFT) and isTruncatedPrime(p, TruncateDirection.RIGHT):
		primeCount += 1
		sum += p

	primeIndex += 1

print sum
	
