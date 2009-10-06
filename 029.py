
terms = dict()

maxValue = 100 
for a in range(2, maxValue+1):
	for b in range(2, maxValue+1):
		value = a**b
		if value in terms:
			terms[value].append((a,b))
		else:
			terms[value] = [(a,b)]

print len(terms)
