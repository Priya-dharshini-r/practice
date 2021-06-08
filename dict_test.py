list1 = ['S1','s2','s3']
list2 = ['aswin','adhi','aanya']
list3 = [85,98,100]
l = len(list1)
l2 = len(list3)

my_dict = {}
my_dict2 = {}

for i in range(l):
	k = list2[i]
	v = list3[i]
	my_dict.update({k:v})

	for j in range(l2):
		k = list1[i]
		my_dict2.update({k:my_dict})

print(my_dict2)


