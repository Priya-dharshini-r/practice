string = "aabb"
# my_dict = dict(string)my

my_dict = {}
for i in string:
	if i in my_dict:
		my_dict[i] += 1
	else:
		my_dict[i] = 1

print(my_dict)

result = ""
for key, value in my_dict.items():
	if value == 1:
		result.join(key)
		break
print(string.index(result))
