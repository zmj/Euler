from zMath import isPandigital

productList = list()

#2 digit x 3 digit = 4 digit
for num1 in range(10, 100):
	for num2 in range(100, 1000):
		product = num1*num2
		if product >= 10000:
			continue

		if isPandigital(9, num1, num2, product) and product not in productList:
			#print str(num1) +" x "+str(num2)+" = "+str(product)
			productList.append(product)

#1 digit x 4 digit = 4 digit
for num1 in range(1, 10):
	for num2 in range(1000, 10000):
		product = num1*num2
		if product >= 10000:
			continue

		if isPandigital(9, num1, num2, product) and product not in productList:
			#print str(num1) + " x "+str(num2)+" = "+str(product)
			productList.append(product)

productSum = 0
for product in productList:
	productSum += product
print productSum
