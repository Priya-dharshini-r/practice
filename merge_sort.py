'''
In merge sort we need to split the array into n havlves, until it has one element in it.
If the array has single element in it, it is aldready sorted.
Then compare each and every element in the array, with next element and arrnge them in sorting order.
Finally combine all elements to a single array.

`'''

def merge(array):
# array = [12, 25, 39, 1, 15, 7, 33, 40]
	if len(array) > 1:
		mid = len(array)//2
		l = array[:mid]
		r = array[mid:]
		merge(l)
		merge(r)

		i = j = k = 0
		while i<len(l) and j<len(r):
			if l[i] < r[j]:
				array[k] = l[i]
				i = i+1
			else:
				array[k] = r[j]
				j = j+1
			k = k+1

		while i<len(l):
			array[k] = l[i]
			i = i+1
			k = k+1
		while j<len(r):
			array[k] = r[j]
			j = j+1
			k = k+1

	return array

if __name__ == "__main__":
	op = merge([12, 25, 39, 1, 15, 7, 33, 40])
	print(op)
