from zMath import allDivisors

def isAmicable(n):
	partner = 0
	for factor in allDivisors(n):
		partner += factor

	if partner == n:
		return False

	nprime = 0
	for factor in allDivisors(partner):
		nprime += factor 
	
	if nprime == n:
		return True
	else:
		return False

max = 10000 
sum = 0
for i in range(2, max+1):
	if isAmicable(i):
		sum += i
print sum
