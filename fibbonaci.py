def fibbonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibbonacci(n-1) + fibbonacci(n-2)


if __name__ == "__main__":
	n = int(input())
	for i in range(n):
		op = fibbonacci(i)
		print(op)
# 0 = 0
# 1 = 1

# n = 5
# 0 1 2 3 4
