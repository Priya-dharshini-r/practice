nums =[1,1,1,1,1]
my_dict = {}

for i in nums:
	if i in my_dict:
		my_dict[i]+=1
	else:
		my_dict[i] = 1
result = []
for key, value in my_dict.items():
	if value <= 1:
		result.append(key)
	else:
		result.append(0)

print(sum(result))
