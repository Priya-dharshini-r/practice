def unique_list(list):
	# return set(list)
	unique_list = []
	for i in list:
		if i not in unique_list:
			unique_list.append(i)
	return unique_list

op  = unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
print(op)
