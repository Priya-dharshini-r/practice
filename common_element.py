list1 = int(input("Enter list1: "))
list2 = int(input("Enter list2: "))
a_list1 = []
a_list2 = []
common = []

i = 0
while i<list1:
	elements = int(input())
	a_list1.append(elements)
	i = i+1
print(a_list1)

j = 0
while j<list2:
	elements = int(input())
	a_list2.append(elements)
	j = j+1
print(a_list2)

i = 0
while i<list1:
	j = 0
	while j<list2:
		if(a_list1[i] == a_list2[j]):
			common.append(a_list1[i])

		j = j+1
	i = i+1
print(common)
