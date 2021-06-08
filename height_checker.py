heights = [1,2,3,4,5]
expected = sorted(heights)
count = 0
n = len(heights)
for i in range(n):
	if heights[i] != expected[i]:
		count = count+1
print(count)
