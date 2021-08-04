'''
number = 788895
count = 0
while number != 0:
	number = number//10
	count = count + 1
print(count)
'''
'''
digits = [1, 2, 3]
n = len(digits)

for i in range(n-1, -1, -1):
	print(digits[i])
	num = digits[i] + 1
	if num>9:
		digits[i] = 0
		if i == 0:
			digits = [1] + digits
		else:
			digits[i] += 1
			break

print(digits)
'''
'''
def my_func(n1, n2):
	return n1+n2

op = my_func(1,2)
print(op)
'''
'''
def func():
	a = 3
	b = 1
	c = 2
	b = b^a^c*2
	if b and c:
		b = 1
		if a:
			a = a*a%5
		c = 0
	print(a+b+c)
func()
'''

for i in range(1,6):
	print(i)
for j in xrange(1,6):
	print(j)
