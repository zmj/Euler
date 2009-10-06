from zMath import PrimeGen

def numQuadraticPrimes(a,b):
	primes = list()
	n = 0
	while True:
		value = n**2 + a*n + b
		if not primeTest.isPrime(value):
			break
		else:
			primes.append(value)
			n += 1
	return len(primes)

primeTest = PrimeGen(25000)
print "Primes Generated"
longestList = 0
longestA = 0
longestB = 0

for a in range(-999, 1000, 1):
	if a==0:
		continue
	for b in range(-999, 1000, 1):
		if b==0:
			continue
		numPrimes = numQuadraticPrimes(a,b)
			
		if numPrimes > longestList:
			longestList = numPrimes
			longestA = a
			longestB = b

print "a: "+str(longestA)+"  b: "+str(longestB)
print "numprimes: "+str(longestList)
print "product: "+str(longestA*longestB)
