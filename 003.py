:close
:q

composite = 600851475143
while True:
	primeFound = False
	for p in range(3, sqrt(composite), 2):
		if composite % p == 0:
			primeFound = True
			composite = composite/p
			break
	if not primeFound:
		print composite
		break
