string = str(input("Enter String : "))
length = len(string)

search_character = input("Enter char : ")

i = 0

while i<length:
	if string[i] == search_character:
		print("$",end = "")
	else:
		print(string[i],end = "")
	i = i+1
print()
