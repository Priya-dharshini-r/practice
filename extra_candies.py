list1 = [2,3,5,1,3]

length = len(list1)

extra_candies = int(input("extra_candies:"))

maximum = max(list1)
print(maximum)
maximum_candies_list = []
for i in list1:
	maximum_candies_list.append(i+extra_candies)
	# print(maximum_candies_list)
print(maximum_candies_list)
result = []
for i in maximum_candies_list:
	if i>=maximum:
		result.append("true")
	else:
		result.append("false")
print(result)
