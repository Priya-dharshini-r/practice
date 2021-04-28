# Initialize a list and get number of elements in the list.
n = int(input("Enter N:"))
a_list = []

# adding elements to the list.
for i in range(0,n):
	elements = int(input())
	a_list.append(elements)
print(a_list)


for i in range(0,n):
	for j in range(n-i-1):
		# Swapping of j element and j+1 element.
		if a_list[j] > a_list[j+1]:
			temp = a_list[j]
			a_list[j] = a_list[j+1]
			a_list[j+1] = temp
		# print(a_list)
print(a_list)
