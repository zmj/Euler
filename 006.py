lim = 100
sum1 = 0
sum2 = 0

for i in range(1,lim+1):
	sum1 += i**2
	sum2 += i
sum2 = sum2**2

print str(sum2) + " - " + str(sum1) + " = " + str(sum2-sum1)
