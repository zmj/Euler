for denominator in range(10, 100):
	for numerator in range(10, denominator):
		numerStr = str(numerator)
		denomStr = str(denominator)

		if numerStr[1] == denomStr[0] and denomStr[1] != '0' and int(numerStr[0]) * 1.0 / int(denomStr[1]) == numerator * 1.0 / denominator:
			print numerStr + "/" + denomStr
