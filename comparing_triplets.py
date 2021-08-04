A = [17, 28, 30]
B = [99, 16, 7]

countA = 0
countB = 0

for i in range(len(A)):
	if A[i] > B[i]:
		countA += 1
	elif A[i] < B[i]:
		countB += 1
	else:
		countA += 0

print(countA, countB) 

