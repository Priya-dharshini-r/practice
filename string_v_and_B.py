v = "coronavirus"
b = "crnas"
count = 0
i = 0
while i<len(b):
	j = 0
	while j<len(v):
		if b[i] == v[j]:
			v = v[j+1:]
			count+=1
			break
		j = j+1
	i = i+1
if count<len(b):
	print("Neg")
else:
	print("pos")
