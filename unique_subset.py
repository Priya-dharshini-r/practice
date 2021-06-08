# list1 = [1,2,3]
# n = 3
# cmp = "000"
# e_l = []
# for i in range(n):
#	if cmp[i] == "1":
#		e_l.append(list1[i])
# print(e_l)

binary_list = ['0','1','10','11','100','101','110','111']
reverse_list = []
for i in range(len(binary_list)):
	reverse_list.append(binary_list[i][::-1])
print(reverse_list)
result = []
for i in range(len(binary_list)):
	# print("Binary",binary_list[i])
	inner_list = []
	for j in range(len(reverse_list[i])):
		if reverse_list[i][j] == "1":
			inner_list.append(list1[j])
	result.append(inner_list)
print(result)

