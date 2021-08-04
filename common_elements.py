list1 = [1, 2, 3, 5, 6]
list2 = [4, 5, 1, 6]

op = []
for i in list1:
	if i in list2:
		op.append(i)

print(op)
