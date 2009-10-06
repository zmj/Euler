from zMath import isPalindrome
from zMath import BaseConvert

def isPalindromeInBinaryAndDecimal(n):
	return isPalindrome(n) and isPalindrome(BaseConvert(n, 2))

sum = 0
for i in range(1, 1000000):
	if isPalindromeInBinaryAndDecimal(i):
		sum += i
print sum
