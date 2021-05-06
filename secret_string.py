def secret_string(string):

	length = len(string)
	empty_string = ""
	for i in range(length):
		# getting the ascii value of each character using ord function.
		value = ord(string[i])
		# adding 5 to each ascii value
		character = value+5
		# getting corresponding character for the added ascii value
		empty_string += chr(character)

	return empty_string

if __name__ == "__main__":
	string = input("Enter string: ")
	op = secret_string(string)
	print("Decoded string:",op)
