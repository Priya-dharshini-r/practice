# input a string and search for a word in a given string and print the number of occurances.

string1 = str(input("Enter string 1 : "))
string2 = str(input("Enter string 2 : "))

length1 = len(string1)
length2 = len(string2)
same = 0

if length1 == length2:
	for i in range (length1):
		if string1 == string2:
			same = same + 1
		else:
			same = 0


	if length1 > same:
		print("False")
	else:
		print("True")

else:
	print("False")
