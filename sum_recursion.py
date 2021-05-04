def sum_of_n_numbers(number):
	if number == 0:
		return 0
	result = number + sum_of_n_numbers(number-1)
	return result

if __name__ == "__main__":
	number = int(input("Enter n: "))
	output = sum_of_n_numbers(number)
	print("Sum of n numbers:",output)
