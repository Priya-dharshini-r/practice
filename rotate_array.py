nums = [1,2,3,4,5,6,7]
k = 3
# xk = k%len(nums)
print("k:", k)
for i in range(k):
	print("Outer Loop")
	previous = nums[-1]
	print("Previous:", previous)
	for j in range(len(nums)):
		print("Inner Loop")
		print("nums[j]:",nums[j])
		nums[j], previous = previous, nums[j]
		print("Swapped Nums:", nums)
print(nums)

