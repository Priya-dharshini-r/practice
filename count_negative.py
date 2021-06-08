grid = [[4,3,-2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
count = 0
m = len(grid)
n = len(grid[0])
for i in range(m):
	for j in range(n):
		if grid[i][j] == -1:
			count = count + 1
print(count)
