queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6]
,[4,3],[1,7]]
king = [3,4]
# [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
outter_list = []
i = 0
while i<8:
	inner_list = []
	j = 0
	while j<8:
		inner_list.append('E')
		j = j+1
	i = i+1
	outter_list.append(inner_list)

# print(outter_list)
for i in range(len(queens)):
	index_0 = queens[i][0]
	index_1 = queens[i][1]
	outter_list[index_0][index_1] = 'Q'
print(outter_list)
final = []

m = king[0]
n = king[1]
i = m
while i<8:
	if outter_list[i][n] == 'Q':
		final.append([i,n])
		break
	i = i+1

m = king[0]
n = king[1]
i = m
while i>=0:
	if outter_list[i][n] == 'Q':
		final.append([i, n])
		break
	i = i-1
m = king[0]
n = king[1]
i = n
while i<8:
	if outter_list[m][i] == 'Q':
		final.append([m, i])
		break
	i = i+1

m = king[0]
n = king[1]
i = n
while i>=0:
	if outter_list[m][i] == 'Q':
		final.append([m, i])
		break
	i = i-1

m = king[0]
n = king[1]
i = m
j = n
while i<8 and j<8:
	if outter_list[i][j] == 'Q':
		final.append([i, j])
		break
	i = i+1
	j = j+1

m = king[0]
n = king[1]
i = m
j = n
while i>=0 and j>=0:
	if outter_list[i][j] == 'Q':
		final.append([i, j])
		break
	i = i-1
	j = j-1

m = king[0]
n = king[1]
i = m
j = n
while i>=0 and j<8:
	if outter_list[i][j] == 'Q':
		final.append([i, j])
		break
	i = i-1
	j = j+1

m = king[0]
n = king[1]
i = m
j = n
while i<8 and j>=0:
	if outter_list[i][j] == 'Q':
		final.append([i,j])
		break
	i = i+1
	j = j-1

print(final)
