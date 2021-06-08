# a_list = [-4,-3,0,1,10]
# result = []
# n = len(a_list)

# for i in range(n):
# 	result.append(a_list[i]*a_list[i])

# y = sorted(result)
# print(y)


# same code using lambda function and divide and conquer.

a_list = [-4, -3, 0, 1, 10]
n = len(a_list)

result = list(map(lambda x: x*x, a_list))
print(result)
i = 0
j = n-1
final = []
while i<=j:
	if result[i]>result[j]:
		final.append(result[i])
		print(final)
		i = i+1
	else:
		final.append(result[j])
		print(final)
		j = j-1
print(final[::-1])
