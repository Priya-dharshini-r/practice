def palindrome(string):
	reverse = ""
	n = len(string)
	j = n-1
	for i in range(n):
		reverse += string[j]
		j = j-1
	if reverse == string:
		return True
	else:
		return False

op = palindrome("helleh")
print(op)
