# Igonore numbers between 6 and 9.
def summer(arr):
	total = 0
	add = True
	for num in arr:
		print("Number:",num)
		while add:
			if num != 6:
				total += num
				print("total:",total)
				break
			else:
				add = False
		while not add:
			if num != 9:
				break
			else:
				add = True
				break
	return total
if __name__ == "__main__":
	array = [2,1,6,9,11]
	print(summer(array))
