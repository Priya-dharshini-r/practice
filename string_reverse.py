import math

# defining a function to reverse a string
def reverse_string(input):
	mylist = list(input)
	length = len(input)
	# floor function n = 8 floor(8/2)>>4
	# floor function n = 7 floor(7/2)>>3
	# only iterating through the half of the string.
	n = math.floor(length/2)
	for i in range(n):
		temp = mylist[i]
		mylist[i] = mylist[length-i-1]
		mylist[length-i-1] = temp
	string = ""
	result = string.join(mylist)
	return result

if __name__ == "__main__":
	input = str(input("Enter string: "))
	output = reverse_string(input)
	print(output)
