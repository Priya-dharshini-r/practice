# Initialize empty array and get input from the user.
list = []

n = int(input("Enter the number of elements:"))
for i in range(n):
	elements = int(input())
	list.append(elements)

print(list)

# Iterate over each element and find the minimum element
for i in range(n):
	min_index = i
	for j in range(i+1, n):
		if(list[min_index] > list[j]): 
			min_index = j


		temp = list[i]
		list[i] = list[min_index]
		list[min_index] = temp

		print(list)
