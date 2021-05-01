import requests

word = input("Which word make you @@##@@: ")
response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en_US/"+word)
result = response.json()

length = len(result[0]['meanings'])

for i in range (length):
	Word = result[0]['word']
	b = result[0]['meanings']
	c = b[i]['partOfSpeech']
	d = b[i]['definitions'][0]['definition']
	# e = b[i]['definitions'][0]['example']

	print("")
	print(c)
	print("\t",d)




# a = result[0]['word']
# b = result[0]['meanings']
# c = b[0]['partOfSpeech']
# d = b[0]['definitions'][0]['definition']
# e = b[0]['definitions'][0]['example']

# a1 = result[0]['meanings']
# b1 = a1[1]['partOfSpeech']
# c1 = a1[1]['definitions'][0]['definition']
# d1 = a1[1]['definitions'][0]['example']


# a2 = result[0]['meanings']
# b2 = a2[2]['partOfSpeech']
# c2 = a2[2]['definitions'][0]['definition']
# d2 = a2[2]['definitions'][0]['example']

# print(a)
# print("")
# print(c)
# print("\t",d)
# print("\t",e)
# print(b1)
# print("\t",c1)
# print("\t",d1)
# print(b2)
# print("\t",c2)
# print("\t",d2)

# print(length)
