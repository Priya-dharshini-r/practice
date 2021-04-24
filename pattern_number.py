# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = int(input("Enter n: "))

i = 0
while i<n:
	j = 0
	while j<=i:
		print(j+1,end = "")
		j = j+1
	i = i+1
	print()

