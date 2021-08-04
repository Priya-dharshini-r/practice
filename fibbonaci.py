'''
def fibbonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibbonacci(n-1) + fibbonacci(n-2)


if __name__ == "__main__":
	n = int(input())
	op = fibbonacci(n)
	print(op)
'''
# 0 = 0
# 1 = 1

# n = 5
# 0 1 2 3 4

# To print in series
# Use for loop give i to the fibonnacci function.
# Need 10 th term, give n directly to the fibbonacci function.
def fibb(n, memo):
	if n in memo:
		return memo[n]
	if n <= 2:
		return 1
	memo[n] = fibb(n-1, memo) + fibb(n-2, memo)
	return memo[n]

if __name__ == "__main__":
	n = int(input("Enter N:"))
	memo = {}
	op = fibb(n, memo)
	print(op)
