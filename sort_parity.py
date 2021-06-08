nums = [3, 1, 2, 4]
even = []
odd = []

for i in range(len(nums)):
	if nums[i]%2 == 0:
		even.append(nums[i])
	else:
		odd.append(nums[i])

print(even+odd)
