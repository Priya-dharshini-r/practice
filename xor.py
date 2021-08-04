nums = [4, 1, 2, 1, 2]
new_list = []
for i in nums:
	if i not in new_list:
		new_list.append(i)
	else:
		new_list.remove(i)
print(new_list.pop())
