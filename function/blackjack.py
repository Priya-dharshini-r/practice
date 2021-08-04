def blackjack(n1,n2,n3):
	total = n1+n2+n3
	if total <= 21:
		return total
	elif total>21 and 11 in (n1,n2,n3):
		return total-10
	else:
		return 'BUST'


if __name__ == "__main__":
	n1,n2,n3 = 9, 9, 11
	print(blackjack(n1,n2,n3))
