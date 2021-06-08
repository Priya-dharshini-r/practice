a_list = [-4,-3,-2,-1,4,3,2]

# OP =[0,-5,-4,1,1,-6]
op_list = [0]

n = len(a_list)
for i in range(n):
	result = op_list[i] + a_list[i]
	op_list.append(result)
	maximum = max(op_list)
print(op_list,maximum)
