def number_in_range(num, low, high):
	list = []
	for i in range(low, high+1):
		list.append(i)
	if num in list:
		return True
	else:
		return False

op = number_in_range(11, 1, 10)
print(op)
