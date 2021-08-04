string = "hello"
vowels = ['a','e','i','o','u']

op = [letter for letter in string if letter not in vowels ]
op = "".join(map(str, op))
print(op)
