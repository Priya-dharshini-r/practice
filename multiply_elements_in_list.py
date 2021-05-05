# defining a function to multiply all the elements in a list
def multiply_all_elements_in_a_list(mylist):
	length = len(mylist)
	result = 1
	for i in range(length):
		element = mylist[i]
		result = result*element
	return result

if __name__ == "__main__":
	n = int(input("Enter number of elements to be in list: "))
	mylist = []
	for i in range(n):
		elements = int(input())
		mylist.append(elements)
	print(mylist)
	multiplied_list = multiply_all_elements_in_a_list(mylist)
	print("Multiplied elements ",multiplied_list)
