current = 1
prev = 1
n = 2
digits = 1000 

while True:
	num = current + prev
	prev = current
	current = num
	n += 1

	if len(str(current)) == digits:
		break

print n
