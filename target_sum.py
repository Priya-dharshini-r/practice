n = int(input("Enter N:"))
a_list = []

for i in range(n):
	a_list.append(int(input()))

target = int(input("Enter target:"))

for i in range(n):

	second_element = target - a_list[i]
	# print("second element + a_list[i]",second_element)


	if second_element in a_list:
		index = a_list.index(second_element)
		print(second_element, a_list[i],index)










