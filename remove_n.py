string = input("Enter the string: ")
# Remove "N" or "n" in a given string and return it
result = " "
for i in string:
    if i != 'n' and i != 'N':
        result += i
print(result)
