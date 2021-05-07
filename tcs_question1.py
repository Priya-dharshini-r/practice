# i = 0

# while i<5:
#	print("i loop: ",i)
#	j = 0
#	while j<3:
#		print("j loop: ",j)
#		j = j+1
#	i = i+1

def sum_list(mylist):
	length = len(mylist)
	sum = 0
	for i in range(length):
		sum+=mylist[i]

	return sum

if __name__ == "__main__":
	n = int(input())
	a_list = []
	for i in range(n):
		elements = int(input())
		a_list.append(elements)
	found = 0
	i = 2
	while i<n and found == 0:
		j = 0

		while j<=n-i and found == 0:
			result = a_list[j:j+i]
			j = j+1
			print(result)
			output = sum_list(result)
			if output == 0:
				found = 1

			# print(output)
		i = i+1
	print(found)

