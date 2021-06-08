import math

list1 = [[1,2,3],[4,5,6],[7,8,9]]
n = len(list1)
# result = 0
# result2 = 0
# odd_length = math.floor(n/2)
p_d = []
s_d = []
for i in range(n):
	result = list1[i][i]
	p_d.append(result)
print("Primary diagonals",sum(p_d))
# secondary diagonal
for i in range(n):
	result2 = list1[i][n-i-1]
	# sum1+=result
	s_d.append(result2)
print("Secondary diagonal",sum(s_d))

final_op = p_d + s_d
print(sum(final_op))
# print(op)

for i in range(n):
	if n%2 == 1:
		position = math.floor(n/2)
		res = list1[position][position]
	print(res)
	result = sum(final_op) - res
print(result)
# for i in range(n):
# 	if n%2 == 1:
# 		result = list1[math.floor(n/2)[i]]
		# result = sum-list1[[math.floor(n/2)[i]]list1[math.floor(n/2)][i]]

# print(result)

















# e_l = []
# for i in final_op:
# 	if i not in e_l:
# 		e_l.append(i)
# print(sum(e_l))

