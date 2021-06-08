# list1 = [1,1,1,1,1]
# op = [1,3,6,10]

n = int(input("Enter n"))
list1 = []

for i in range(n):
	list1.append(int(input()))

return_list = []
sum = 0

for i in range(n):
	# slice = list1[i:i]
	# return_list.append(list1[i-1]+list[i])
	sum = sum + list1[i]
	return_list.append(sum)
	# print(sum)
print(return_list)
