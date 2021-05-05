# Given a number n return true if 10 is present within either 100 or 200.

def almost_there(num):
	if ((abs(100-num)<=10) or (abs(200-num)<=10)):
		return True
	else:
		return False

if __name__ == "__main__":
	num = int(input())
	op = almost_there(num)
	print(op)
