from zMath import PrimeGen
import sets

primes = PrimeGen(1000000)
print "Primes generated"
n = 4 
current = range(1, n+1)

while True:
	allValid = True
	for num in current:
		if len(primes.distinctPrimeFactors(num)) != n:
			allValid = False
			break

	if allValid:
		break
	else:
		del current[0]
		current.append(current[-1]+1)

print current[0]
