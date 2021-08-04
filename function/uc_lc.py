def string(s):
	u_count = 0
	l_count = 0
	for i in s:
		if i>='A' and i<='Z':
			u_count += 1
		if i>='a' and i<='z':
			l_count += 1

	return u_count,l_count

result = string("Hello Mr. Rogers, how are you this fine Tuesday?")
print(result)
