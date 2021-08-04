nums = [1,2,3,1]
k = 3

my_dict = {}
for i, value in enumerate(nums):
	if value in my_dict and i-my_dict[value] <= k:
		print("True")
	my_dict[value] = i
	print("My_dict[values]",i)
print("False")
