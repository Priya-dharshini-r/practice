n = 6
a_list = []
k = 5
for i in range(1, n+1):
	a_list.append(i)

i = 0
count = 1
while len(a_list)>1:
	if count != k:
		count = count+1
		i = i+1
	else:
		a_list.pop(i)
		count = 1
	if i == len(a_list):
		i = 0
print(a_list[0])
