def volume_of_sphere(rad):
	# 4/3 pi * r^3
	pi = 3.14
	volume = (4/3)*pi*rad*rad*rad
	return volume

op = volume_of_sphere(2)
print(op)
