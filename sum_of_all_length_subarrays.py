a_list = [1,4,2,5,3]
n = len(a_list)
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15

# 1+4+2+5+3+7+11+10+15 = 58

# for i in range(5]
i = 0

while i <n:

	j = 0
	while j<n-i:
		result = a_list[j:j+i]
		j = j+1
	i = i+1
	print(result)
