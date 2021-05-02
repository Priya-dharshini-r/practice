def get_string_occurances(string,search_string):
	length1 = len(string)
	length2 = len(search_string)
	count = 0
	for i in range(length1):
		sample = string[i:i+length2]
		if sample == search_string:
			count = count+1
	return count

if __name__ == "__main__":
	string = str(input("Enter string: "))
	search_string = str(input("search_word"))
	output = get_string_occurances(string,search_string)
	print(output)
