# Remove duplicates from the sorted array.
# Inplace and no extra place.

nums = [1, 1, 2]
i = 0
for j in range(1, len(nums)):
	if nums[i] != nums[j]:
		i = i+1
		nums[i] = nums[j]
i = i+1
print(nums)
