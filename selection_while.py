# ask the user how many numbers oof elements in list.
n = int(input("Enter n: "))

# Initialize a list and get each value using while loop.
list1 = []

i = 0
while i<n:
	elements = int(input())
	list1.append(elements)
	i = i+1
print(list1)

# Sorting
i = 0
while i < n:
	min_pos = i

	j = i+1
	while j < n: #{

		if list1[min_pos] > list1[j]:
			min_pos = j
		j = j+1
	# }
# swapping of min_pos and i
	temp = list1[min_pos]
	list1[min_pos] = list1[i]
	list1[i] = temp


	i = i+1


print(list1)
