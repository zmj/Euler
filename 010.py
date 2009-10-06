from zMath import PrimeGen

primes = PrimeGen(2000000)
sum = 0
for p in primes.primes:
	sum += p
print sum
