import collections
list1 = [2,14,18,22,22]
dictionary = collections.Counter(list1)
print(dictionary)

for key, value in dictionary.items():
	if value > 1:
		print("true")
	else:
		print("false")
