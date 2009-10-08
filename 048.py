n = 1000

sum = 0
for i in range(1, n+1):
	sum += i**i

s = str(sum)
print s[-10:len(s)]
