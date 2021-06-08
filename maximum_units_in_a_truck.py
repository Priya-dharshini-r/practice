boxTypes = [[5, 10],[2, 5],[4, 7],[3, 9]]
trucksize = 10

# sort the box type by it's maximum number of units
sorted_boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
print(sorted_boxTypes)

r_box = trucksize
loaded_units = 0
i = 0
while r_box>0 and i<len(sorted_boxTypes):
	if sorted_boxTypes[i][0] <= r_box:
		loaded_units += sorted_boxTypes[i][0] * sorted_boxTypes[i][1]
		r_box -= sorted_boxTypes[i][0]
	else:
		loaded_units += r_box * sorted_boxTypes[i][1]
		r_box = 0
	i = i+1
print(loaded_units)
