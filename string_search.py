# input a string and search for a word in a given string and print the number of occurances.

string1 = str(input("Enter string 1 : "))
search_string = str(input("Search String : "))
length1 = len(string1)
length2 = len(search_string)
count = 0

for i in range (length1):
	sample = string1[i:i+length2]

	if sample == search_string:
		count = count+1
print(count) 
