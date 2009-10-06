from zMath import factorial

numStr = str(factorial(100))
sum = 0
for c in numStr:
	sum += int(c)
print sum
