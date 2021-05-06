# Accept a it has only twpo words and return true if the first and second word is same. 
def animal_cracker(string1):
	list1 = string1.split()

	if list1[0][0] == list1[1][0]:
		return True
	else:
		return False

if __name__ == "__main__":
	string1 = str(input("Enter a string:"))
	output = animal_cracker(string1)
	print("Is both same:",output)
