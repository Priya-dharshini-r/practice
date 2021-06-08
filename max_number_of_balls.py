low_limit = 5
high_limit = 15
my_dict = {}
for nums in range(low_limit, high_limit+1):
	print(nums)
	sum = 0
	for i in str(nums):
		# print(i)
		sum = sum + int(i)
	if sum in my_dict:
		my_dict[sum] += 1
	else:
		my_dict[sum] = 1
op = max(my_dict.values())
print(op)
