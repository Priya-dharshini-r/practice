week = ['Mon','Tue','wed','thur','fri']
n = 14
for i in range(n):
	day = i%len(week)
	print(week[day])
