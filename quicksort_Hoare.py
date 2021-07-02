def partition(arr, start, end):
	pIndex = start
	pivot = arr[pIndex]

	while start<end:
		while start < len(arr) and arr[start] <= pivot:
			start += 1
		while arr[end] > pivot:
			end -= 1
		if start < end:
			arr[start], arr[end] = arr[end], arr[start]

	arr[pIndex], arr[end] =  arr[end], arr[pIndex]
	return end

def quicksort(arr, start, end):
	if start<end:
		pi = partition(arr, start, end)

		quicksort(arr, start, pi-1)
		quicksort(arr, pi+1, end)


if __name__ == "__main__":
	arr = [45, 78, 3, 1, 90, 29]
	op = quicksort(arr, 0, len(arr)-1)
	print(arr)
