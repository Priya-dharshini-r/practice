n = int(input("Enter Number of elements in the list: "))

a_list = []

i = 0
while i<n:
	elements = int(input())
	a_list.append(elements)
	i = i+1
print(a_list)

i = 0
while i<n:
	j = 0
	while j<n-i-1:
		if a_list[j] > a_list[j+1]:
			a_list[j], a_list[j+1] = a_list[j+1], a_list[j]

		j = j+1
	i = i+1

print(a_list)
