def isSumOfExp(n):
	sum = 0
	for digitChr in str(n):
		digit = int(digitChr)
		sum += digit**exponent
	return sum == n

sum = 0
maxTest = 10000000
exponent = 5 

for i in range(10,maxTest):
	if isSumOfExp(i):
		sum += i

print sum
