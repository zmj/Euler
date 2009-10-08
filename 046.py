from zMath import PrimeGen
from math import sqrt

maxNum = 10000
primes = PrimeGen(maxNum)
print "Primes generated"
composite = 3
while True:
	if primes.isPrimeHash(composite):
		composite += 2
		continue

	found = False
	for sq in range(1, int(sqrt(composite))):
		primeDifference = composite - 2*sq**2
		if primes.isPrimeHash(primeDifference):
			#print str(composite) + " = "+str(sq)+"^2 + " + str(primeDifference)
			found = True
			break

	if not found or composite > maxNum:
		print composite
		break
	else:
		composite += 2
