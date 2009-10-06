from zMath import PrimeGen
from zMath import isPandigital

primes = PrimeGen(100000000)
for i in range(len(primes.primes)-1, 0, -1):
	prime = primes.primes[i]
	if isPandigital( len(str(prime)), prime):
		print prime
		break
