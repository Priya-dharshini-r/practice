string = str(input("Input String : "))

# length = len(string)
# converted_list = list(string)
# print(converted_list)

my_dict = {}
i = 0
for i in string:
	if i in my_dict:
		# print(my_dict)
		my_dict[i] += 1
		# print(my_dict)
	else:
		my_dict[i] = 1
		# print(my_dict)
print(my_dict)


