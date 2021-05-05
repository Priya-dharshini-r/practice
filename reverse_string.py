def reverse_words_in_string(string):
	# Converting string to list using split method
	string_list = string.split()
	length = len(string_list)
	reversed_list = []

	for i in range(length):
		# Grabing the last word in a string
		result = string_list[length-i-1]
		reversed_list.append(result)
	empty_string = " "
	output = empty_string.join(reversed_list)

	return output

if __name__ == "__main__":
	string = str(input("Enter string: "))
	final_output = reverse_words_in_string(string)
	print(final_output)
