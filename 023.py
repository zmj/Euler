from zMath import allDivisors

def isAbundant(n):
	sum = 0
	for factor in allDivisors(n):
		sum += factor
	if sum > n:
		return True
	else:
		return False

abundants = list()
for i in range(1, 28124):
	if isAbundant(i):
		abundants.append(i)

#has to be a better way to do this
sum = 0
bads = list()
for n in range(1, 28124):
	foundSum = False
	for abun in abundants:
		if abun > n:
			break

		diff = n - abun
		if abundants.count(diff)>0:
			foundSum = True
			break
	if not foundSum:
		sum += n
		bads.append(n)
print sum
