input_string = str(input("Input_string: "))
search_word = str(input("Search_word :"))
search_character = str(input("Enter seach character: "))

# Counting frequency Of each character in a given string and stored in a dictionary.
my_dict2 = {}
for i in input_string:
	if i in my_dict2:
		my_dict2[i]+=1
	else:
		my_dict2[i] = 1
print(my_dict2)

# Counting frequency of each word in a given string and stored in a dictionary.
my_dict = {}
each_word = input_string.split()
for word in each_word:
	if word in my_dict:
		my_dict[word]+=1
	else:
		my_dict[word] = 1

print(my_dict)

# print the key and value of repeated word.
for key,value in my_dict.items():
	if key == search_word:
		print("The word",key,"is occurred",value,"times.")
	else:
		print("Not Found")
		break

# print value of repeated character.
for key, value in my_dict2.items():
	if key == search_character:
		print("The letter",key,"is occured",value,"times.")
	else:
		print("Not Found")
		break
