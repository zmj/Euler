from zMath import PentagonalNumbers
import sys

numBelow = 10000000
pentNums = PentagonalNumbers(numBelow)
print "Pent Numbers generated"
for pentNum1 in pentNums.numbers:
	for pentNum2 in pentNums.numbers:
		if pentNum1 == pentNum2:
			continue
		sum = pentNum1 + pentNum2
		diff = max(pentNum1, pentNum2) - min(pentNum1, pentNum2)
		if pentNums.isPent(sum) and pentNums.isPent(diff):
			#print "Testing: "+str(pentNum1)+","+str(pentNum2)+": "+str(sum)+","+str(diff)
			print diff
			sys.exit(0)
