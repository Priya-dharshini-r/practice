nums = [24,69,100,99,79,78,67,36,26,19]
n = len(nums)
lower_bound = 0
upper_bound = n-1

while lower_bound<=upper_bound:
	mid = (lower_bound + upper_bound) // 2
	value1 = nums[mid] - nums[mid-1]
	# print("mid:",mid,"Value1:",value1)
	value2 = nums[mid+1] - nums[mid]
	# print("Value2:",value2)
	if value1>0 and value2<0:
		print(mid)
		break
	elif value1>0 and value2>0:
		lower_bound = mid+1
	elif value1<0 and value2<0:
		upper_bound = mid-1

