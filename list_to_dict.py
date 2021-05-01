list1 = ['S001','S002','S003','S004','S005']
list2 = ['Adina Park','Leyton Marsh','Duncan Boyle','Saim Richards','Ian Somhandeler']
list3 = [85,98,89,92,100]

length = len(list1)
# mydict = {}
# mydict2 = {}
# mydict3 = {}
# mydict4 = {}

mylist = []

# mydict = {list1[0]:{list2[0]:list3[0]}}
# mydict2 = {list1[1]:{list2[1]:list3[1]}}
# mydict3 = {list1[2]:{list2[2]:list3[2]}}
# mydict4 = {list1[3]:{list2[3]:list3[2]}}
for i in range(length):
	mydict = {list1[i]:{list2[i]:list3[i]}}
	mylist.append(mydict)


print(mylist)

