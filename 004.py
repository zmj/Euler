from zMath import isPalindrome

biggestPal = 0
for x in range(100,999):
	for y in range(100,999):
		pal = x*y
		if isPalindrome(pal) and biggestPal < pal:
			biggestPal = pal

print biggestPal
			
