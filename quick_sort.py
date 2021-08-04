'''
Lomuto Partion.

Condition for quick sort:
Let's taeke an element pivot, and all the elements left to pivot is less than pivot and all the elements right to pivot is greater than pivot.

The main core for the quick sort is the partion.

1. Make the last element as pivot and partion index as start.
2. Traverse to the array, check if the ith element is less than or equal to pivot element.
3. if the ith element is smaller, swap it with partion index. Increment the partion index.
4. After all the swapping is done with ith and partion index, swap the end element and partion index.

'''

# Lomuto partion
# def partion(array, start, end):
array = [10,7,8,9,1,5]
n = len(array)
print("Length",n)
start = 0
end = n-1
pivot = array[end]
print("Pivot", pivot)
p_index = start

for i in range(n-1):
	print("i:",i)
	if array[i] <= pivot:
		print("array[i]:",array[i],"pivot", pivot)
		array[i], array[p_index] = array[p_index], array[i]
		p_index += 1
# swapping pivot and partion index

array[end], array[p_index] = array[p_index], array[end]
print(array)

'''
Hoare Partion:

Most cases first element is pivot element.

1. Make 2nd element as start is 'i' and last is 'j' element as end.
2. Compare the ith element with pivot element, if the ith element is greater than pivot element, pause the i there.
3. Now compare the pivot with element in j index, if the jth element is less than pivot swap i and j element.
4. On moving forward we have to increment the j and for j decrement the j.
5. Once if j crossed i swap the j and pivot element.

'''
# Hoare Partion
array = [10, 7, 9, 8, 1, 5]
n = len(array)
print("length:", n)
start = 0
end = n-1
pIndex = start
pivot = array[pIndex]
while start<end:
	# print("Start:", start, "End:", end)
	# print("array[start]:", array[start], "array[end]:", array[end])
	while start < len(array) and array[start] <= pivot:
		start += 1

	while array[end] > pivot:
		end -= 1

	if start<end:
		array[start], array[end] = array[end], array[start]

array[pIndex], array[end] = array[end], array[pIndex]
print(array)






























