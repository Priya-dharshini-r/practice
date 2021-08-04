def paper_doll(string):
	result = ""
	for char in string:
		result += char*3
	return result

if __name__ == "__main__":
	string = input("Enter the string to be in paper doll: ")
	op = paper_doll(string)
	print(op)
