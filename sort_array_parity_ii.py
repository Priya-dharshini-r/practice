list1 = [4,2,5,7]
n = len(list1)
even = []
odd = []
for i in range(n):
	if list1[i]%2 == 0:
		even.append(list1[i])
	else:
		odd.append(list1[i])
final = []
for i in range(int(n/2)):
	final.append(even[i])
	final.append(odd[i])

print(final)
