maxNum = 1000999
numbers = list()

for i in range(1, maxNum+1):
	numbers.append(str(i))

numStr = ''.join(numbers)
product = 1
for x in range(0, 7):
	product *= int( numStr[ 10**x - 1 ] )

print product
