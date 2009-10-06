from zMath import factorial

def permuteLexi(sequence): #sequence of pre-sorted things, smallest to largest, returns list of lists
	permutations = list()
	seqLength = len(sequence)
	if seqLength==1:
		permutations.append([sequence[0]])
		return permutations
	else:
		for num in sequence:
			subSequence = list(sequence)			
			subSequence.remove(num)
			subPerms = permuteLexi(subSequence)
			for subPerm in subPerms:
				subPerm.insert(0, num)
				permutations.append(subPerm)
		return permutations

#wrong way
#millionPerms = permuteLexi(range(0,10))
#print millionPerms[999999]

n = 10 
origSequence = range(0,n)
sequence = list(origSequence)
x = 999999

perm = list()
for i in range(0, n):
	f = factorial(n-i-1)
	div = x / f
	perm.append(str(sequence[div]))
	del sequence[div]
	x -= div*f

print ''.join(perm) 
	
