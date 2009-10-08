from zMath import TriangleNumbers
from zMath import PentagonalNumbers
from zMath import HexagonalNumbers

maxNum = 10000000000
tri = TriangleNumbers(maxNum)
pent = PentagonalNumbers(maxNum)
hex = HexagonalNumbers(maxNum)

for num in tri.numbers:
	if pent.isPent(num) and hex.isHex(num):
		print num
