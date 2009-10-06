from zMath import factorial

maxExp = 1
while True:
	if factorial(9)*maxExp < 10**maxExp:
		break
	else:
		maxExp += 1


def isSumOfDigitFactorial(n):
	sum = 0
	for digitChr in str(n):
		digit = int(digitChr)
		sum += factorial(digit)
		if sum > n:
			return False
	return sum == n

sum = 0
for i in range(10, 10**(maxExp-1)):
	if isSumOfDigitFactorial(i):
		sum += i

print sum
