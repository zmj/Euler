coins = [ 1, 2, 5, 10, 20, 50, 100, 200 ]
desired = 200

def doMagic(amountRemaining, previousCoin):
	if amountRemaining == 0:
		return [[]]

	next = list()
	for coin in coins:
		if amountRemaining >= coin and previousCoin >= coin:
			for subNext in doMagic(amountRemaining-coin, coin):
				next.append( [coin] + subNext )

	return next

result = doMagic(desired, coins[-1])
print len(result)	
