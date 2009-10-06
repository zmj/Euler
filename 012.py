from zMath import allFactors
import sys

sum = 0
n = 1
while True:
	sum += n
	if len(allFactors(sum)) > 500:
		print sum
		sys.exit()
	n += 1	
