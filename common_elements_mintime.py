# Printing common elements in both the list with minimum time complexity.
list1 = int(input("Enter n: "))
list2 = int(input("Enter n: "))
a_list1 = []
a_list2 = []
common = []
my_dict = {}

i = 0
while i<list1:
	elements = int(input())
	a_list1.append(elements)
	i = i+1
print("List 1-",a_list1)

j = 0
while j<list2:
	elements = int(input())
	a_list2.append(elements)
	j = j+1
print("List 2-",a_list2)

# "+" symbol will merges two lists
merged_list = a_list1 + a_list2
print("Concated List-",merged_list)

for i in merged_list:
	if i in my_dict:
		my_dict[i]+=1
	else:
		my_dict[i] = 1
print("Frequencies of a number representing in dictionary-",my_dict)

# print all the keys if value is greater than 1

for key, value in my_dict.items():
	if value > 1:
		common.append(key)
print("Common Elements in both the list-",common)

