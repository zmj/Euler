from math import sqrt
from zMath import isInt
import sys

for c in range(5, 1000):
	for b in range(2, c):
		a = sqrt(c**2 - b**2)
		if isInt(a):
			if a+b+c == 1000:
				print int(a*b*c)
				sys.exit()
