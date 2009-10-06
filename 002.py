sum=0;
nMinusOne=0;
n=1;
count = 0;
while n <= 4000000:
	if n % 2 == 0:
		sum += n;
	newVal = nMinusOne + n;
	nMinusOne = n;
	n = newVal;
	count += 1;
print sum;
