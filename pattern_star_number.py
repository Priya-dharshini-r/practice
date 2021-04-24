n = int(input("Enter N: "))

i = 0
while i<n:
	j = 0
	count = n-i-1
	print(count*"* " , end= "")
	while j<=i:
		print(i+1,end =" ")
		j = j+1
	i = i+1
	print()

