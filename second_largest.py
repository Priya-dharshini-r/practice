def second_largest(mylist):

	maximum = float('-inf')
	maximum_index = 0
	length = len(mylist)
	for i in range(length):
		if mylist[i] > maximum:
			maximum = mylist[i]
			maximum_index = i
	mylist[maximum_index] = float('-inf')

	second_max = float('-inf')
	for i in range(length):
		if mylist[i] > second_max:
			second_max = mylist[i]
	return second_max

if __name__ == "__main__":
	n = int(input("Enter N: "))
	a_list = []
	for i in range(n):
		elements = int(input())
		a_list.append(elements)
	output = second_largest(a_list)
	print(output)
