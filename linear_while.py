n = int(input("Enter n : "))

a_list = []

i = 0
while i < n:
	elements = int(input())
	a_list.append(elements)
	i = i+1
print(a_list)

i = 0
search_element = int(input("Enter search element: "))
found = False
while i < n:

	if a_list[i] == search_element:
		found = True
		print("Element found at index",i)

	i = i+1

if found == False:
	print("Element not found")
