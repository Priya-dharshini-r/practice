string1 = "Hello"
string_list = list(string1)
# print(string_lis(t)
result = []
n = len(string_list)
for i in range(n):
	result.append(string_list[n-i-1])
print(result)
op = "".join(map(str, result))

print(op)
