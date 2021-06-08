input = "aaaabbbbcccc"
min = 'a'
max = 'z'
str3 = ""

my_dict = {}
sorted_input = str3.join(sorted(input))
# print(sorted_input)
for i in sorted_input:
	if i in my_dict:
		my_dict[i]+=1
	else:
		my_dict[i] = 1
print(my_dict)

result = ""
while len(input) != len(result):
	for key, value in my_dict.items():
		if value != 0:
			result+=key
			my_dict[key] = value-1
# print(result)
	for key, value in reversed(my_dict.items()):
		if value != 0:
			result+=key
			my_dict[key] = value-1
print(my_dict)
print(result)
