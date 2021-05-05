# return true if n1 and n2 is 20 or any n1 or n2 = 20

def make_twenty(n1, n2):
	sum = n1+n2
	if sum == 20 or n1 == 20 or n2 == 20:
		return True
	else:
		return False

if __name__ == "__main__":
	n1 = int(input())
	n2 = int(input())
	op = make_twenty(n1, n2)
	print(op)
