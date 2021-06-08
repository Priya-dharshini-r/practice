#      [0, 1,2,3,4, 5,6]
nums = [-1,0,3,5,9,12,17]
target = 17
n = len(nums)
lower_bound = 0
upper_bound = n - 1

while lower_bound <= upper_bound:
	print("lower_bound:",lower_bound)
	print("upper_bound:",upper_bound)
	mid = (lower_bound + upper_bound) // 2
	print("mid:",mid)
	if nums[mid] == target:
		print("Found at:",mid)
		break
	else:
		if nums[mid] < target:
			lower_bound = mid+1
			print("lower_mid:",nums[mid])
		else:
			upper_bound = mid-1
			print("upper_mid:",nums[mid])
