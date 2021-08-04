# Given an array of digits add one to the digits

# Eg: Digits = [1, 2, 3] --> Int = 123
# Ex.Op = [1, 2, 4] --> Int = 124

digits = [1, 2, 3]
# Used map of function to convert all int in a list to string and concate to it.
string = "".join(map(str, digits)) # String = "123"
# Convert string to int
integer = int(string) + 1
print(integer)

# Integer to list again
output = list(str(integer))
print(output)
