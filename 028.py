def spiralCorners(n):
	bigCorner = n**2
	decrement = n-1
	corners = list()
	for i in range(0, 4):
		corners.append(bigCorner - i*decrement)

	return corners

sum = 1
spiralSize = 1001 
for i in range(3, spiralSize+2, 2):
	corners = spiralCorners(i)
	for cornerValue in corners:
		sum += cornerValue

print sum
