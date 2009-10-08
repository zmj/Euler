from zMath import PrimeGen

maxNum = 1000000
primegen = PrimeGen(maxNum)
longestChain = 0
resultingPrime = 0
for primeIndex in range(0, len(primegen.primes)):
	chain = 0
	sum = 0
	while sum<maxNum and primeIndex+chain<len(primegen.primes):
		if primegen.isPrimeHash(sum) and chain>longestChain:
			longestChain = chain
			resultingPrime = sum

		sum += primegen.primes[primeIndex+chain]
		chain += 1

#print longestChain
print resultingPrime
		
