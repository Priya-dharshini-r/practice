# leeser of two evens

def lesser_of_two_evens(a,b):
	if a%2 == 0 and b%2 == 0:
		return min(a,b)
	else:
		return max(a,b)

if __name__ == "__main__":
	a = int(input("Enter a:"))
	b = int(input("Enter b:"))
	output = lesser_of_two_evens(a, b)
	print("Less of two evens:",output)
