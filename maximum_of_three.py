def maximum_of_three_numbers(num1,num2,num3):
	if num1>num2 and num1>num3:
		return num1
	elif num2>num3 and num2>num1:
		return num2
	else:
		return num3

if __name__ == "__main__":
	num1 = int(input("Enter number1: "))
	num2 = int(input("Enter number2: "))
	num3 = int(input("Enter number3: "))
	result = maximum_of_three_numbers(num1,num2,num3)
	print("Maximum of three number is ",result)
