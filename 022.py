def score(name):
	sum = 0
	for c in name:
		sum += ord(c) - ord('A') + 1
	return sum

file = open("names.txt")
names = file.read().split(",")
for i in range(0, len(names)):
	names[i] = names[i][1:-1]

names.sort()
scoreSum = 0
for i in range(1, len(names)+1):

	name = names[i-1]
	scoreSum += i * score(name)
print scoreSum
