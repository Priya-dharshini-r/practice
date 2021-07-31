#      [0, 1,2,3,4, 5,6]
nums = [-1,0,3,5,9,12,17]
search = -1
n = len(nums)
low = 0
upper = n-1

while low <= upper:
	mid = (low+upper) // 2
	if nums[mid] == search:
		print("Element at index:",mid)
		break
	elif nums[mid] < search:
		lower =  mid + 1
	else:
		upper = mid - 1


