month = int(input("Enter month: "))
week = int(input("Enter week: "))


k = 1
while k<=month:
	print("Month:",k)
	i = 1
	# odd
	while i<=week:
		if(i%2 == 1):
			print("\tWeek:",i)
			j = 1
			# even
			while j<8:
				if(j%2 == 0):
					print("\t\tDay:",j)
				j = j+1
		i = i+1
	k = k+1
