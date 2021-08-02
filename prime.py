def prime(n):
	for num in range(n+1):
		if num>1:
			for prime in range(2, num):
				if(num%prime) == 0:
					break
			else:
				yield num

if __name__ == "__main__":
	number = int(input("Enter the number:"))
	for i in prime(number):
		print(i)
