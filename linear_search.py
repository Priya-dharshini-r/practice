# Initialize a empty list and get elements from the user.
list = []
n = int(input("Enter number of elements:"))

# Use a for loop to get each element in the list.
for i in range(n):
	elements = int(input())
	list.append(elements)
print(list) 

# Ask the element to be searched.
search_element = int(input("Enter the element to be searched:"))

# set element_found as false
element_found = False

# Compare the given element to each element in the list by its index position.
# if the serached element and the list element are same return "Element-found" and its index position.
# if element_found is false print "Element-not-found".
for i in range(n):
	if(list[i] == search_element):
		element_found = True
		print("Element found at index",i)
		break


if(element_found == False ):
	print("Element not found")
