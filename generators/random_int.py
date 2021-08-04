import random
# print(random.randint(1,10))
def rand_num(low, high, n):
	for i in range(n):
		yield random.randint(low, high)

for i in rand_num(1,10,12):
	print(i)
