integer = 12345
op = []
while integer>0:
	op.insert(0, integer%10)
	integer = integer // 10
print(op)
