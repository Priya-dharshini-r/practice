def partition(array, start, end):
	n = len(array)
	pivot = array[end]
	pIndex = start
	for i in range(start, end):
		if array[i] <= pivot:
			array[i], array[pIndex] = array[pIndex], array[i]
			pIndex += 1
			print(array)
	array[pIndex], array[end] = array[end], array[pIndex]
	print(array)
	return pIndex

def quick_sort(array, start, end):
	if len(array) == 1:
		return

	if start<end:
		pi = partition(array, start, end)
		print(array)
		quick_sort(array, start, pi-1)
		print(array)
		quick_sort(array, pi+1, end)
		print(array)

if __name__ == "__main__":
	array = [10, 7, 8, 9, 1, 5]
	n = len(array)
	p = quick_sort(array, 0, n-1)
	print(array)
