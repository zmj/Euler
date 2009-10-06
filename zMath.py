from math import sqrt

def nthLexiPerm(sequence, n):
	perm = list()
	seq = list(sequence)
	seqLength = len(sequence)
	for i in range(0, seqLength):
		f = factorial(seqLength-i-1)
		div = n / f
		perm.append(str(seq[div]))
		del seq[div]
		n -= div*f
	return ''.join(perm)

def isPandigital(n, *numbers):
	availableDigits = range(1, n+1)
	
	for num in numbers:
		for digitChr in str(num):
			digit = int(digitChr)
			if digit in availableDigits:
				availableDigits.remove(digit)
			else:
				return False
	return True

def factorial(x):
	if x <= 1:
		return 1
	else:
		product = 1
		for i in range(1, x+1):
			product *= i
		return product

def isPalindrome(p):
	p = str(p)
	for i in range(0, len(p)/2):
		if p[i] != p[-1*(i+1)]:
			return False
	return True

def BaseConvert(n, base): 
	'''converts from base 10 to string rep of # in specified base'''
	numDigits = 0
	while True:
		if base**numDigits > n:
			break
		else:
			numDigits += 1

	digits = list()
	for place in range(numDigits-1, -1, -1):
		value = base**place
		digit = n / value
		digits.append(str(digit))
		n -= digit*value

	return ''.join(digits)

def isInt(x):
	return int(x) == x

def allDivisors(x):
	l = allFactors(x)
	l.remove(x)
	return l

def allFactors(x):
	factors = list()
	factors.append(1)
	factors.append(x)

	for i in range(2,int(sqrt(x))+1):
		if x % i == 0:
			factors.append(i)
			factor = x/i
			if factor != i:
				factors.append(factor)
	return factors

def isPrimeSimple(p):
	if p % 2 == 0:
		return False

	for i in range(3, int(sqrt(p)), 2):
		if p % i == 0:
			return False
	return True

class PrimeGen:
	primes = list()
	
	def __init__(self, primesBelow):
		self.primes.append(2)
		for p in range(3, primesBelow, 2):
			if self.isPrime(p):
				self.primes.append(p)
	
	def isPrime(self, p):
		if p <= 1:
			return False

		limit = sqrt(p)
		for prime in self.primes:
			if prime > limit:
				return True
			elif p % prime == 0:
				return False
		return True
