from zMath import isPandigital

upperBound = 9999 

for i in range(upperBound, 0, -1):
	products = list()
	productConcatLength = 0

	n = 1
	while True:
		if productConcatLength>=9:
			break
		product = str( n * i )
		products.append(product)
		productConcatLength += len(product)
		n += 1

	if productConcatLength>9:
		continue
	
	if isPandigital(9, *products):
		print ''.join(products)
		break	
