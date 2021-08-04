list1 = [1, 2, 3, 4, 5]
# op = list1[::-1]
# print(op)
n = len(list1)
for i in range(0, int(n//2)):
	print("$$$$$$$")
	list1[i], list1[n-i-1] = list1[n-i-1], list[i]

print(list1)
