def array(nums):
	for i in range(len(nums)-1):
		if nums[i] == nums[i+1]:
			return True
	return False

if __name__ == "__main__":
	nums = [1,3,3]
	print(array(nums))
