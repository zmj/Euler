from math import sqrt
import sets

class PentagonalNumbers:
	numbers = set()

	def __init__(self, pentNumbersBelow):
		n = 1
		while True:
			nextPent = (n*(3*n-1))/2
			if pentNumbersBelow < nextPent:
				break
			else:
				self.numbers.add(nextPent)
				n += 1

	def isPent(self, n):
		return n in self.numbers

class TriangleNumbers:
	numbers = set()

	def __init__(self, triangleNumbersBelow):
		n = 1
		while True:
			nextTri = (n*(n-1))/2
			if triangleNumbersBelow < nextTri:
				break
			else:
				self.numbers.add(nextTri)
				n += 1

	def isTri(self, n):
		return n in self.numbers

class HexagonalNumbers:
	numbers = set()

	def __init__(self, hexNumbersBelow):
		n = 1
		while True:
			nextHex = n*(2*n - 1)
			if hexNumbersBelow < nextHex:
				break
			else:
				self.numbers.add(nextHex)
				n += 1

	def isHex(self, n):
		return n in self.numbers

def unorderedSequenceEqual(seq1, seq2):
	return frozenset(seq1) == frozenset(seq2)

def numericPermutations(number, n=0):
	perms = permutations(str(number), n)
	permNums = list()
	for perm in perms:
		permNums.append( int( ''.join(perm) ) )
	return permNums

def permutations(sequence, n=0):
	if len(sequence) == n:
		return [[]]
	
	perms = list()
	for item in sequence:
		seqCopy = list(sequence)
		seqCopy.remove(item)
		for subPerm in permutations(seqCopy, n):
			perms.append( [item] + subPerm )

	return perms

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
	primeHash = set()
	
	def __init__(self, primesBelow):
		self.primes.append(2)
		for p in range(3, primesBelow, 2):
			if self.isPrime(p):
				self.primes.append(p)
				self.primeHash.add(p)
	
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

	def isPrimeHash(self, p):
		return p in self.primeHash

	def distinctPrimeFactors(self, n):
		return set(self.allPrimeFactors(n))

	def allPrimeFactors(self, n):
		if n==1:
			return []

		for prime in self.primes:
			if prime > n:
				break
			if n % prime == 0:
				return [ prime ] + self.allPrimeFactors(n/prime)
		
