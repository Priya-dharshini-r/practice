# from random module import shuffle package to suffle the list at any manner
from random import shuffle

# Initial list
def initial_list():
	mylist = ['O','','']
	return mylist

def shuffle_list(mylist):
	shuffled_list = shuffle(mylist)
	return shuffled_list

def player_guess():
	guess = ''
	while guess not in ['0','1','2']:
		guess = input("Pick a position 0,1,2: ")
	return int(guess)

def check_guess(result,guess):
	if result[guess] == 'O':
		print("Correct")
		print(result)
	else:
		print("oops!! Not here")
		print(result)

if __name__ == "__main__":
	result = initial_list()
	# print(result)
	shuffled = shuffle_list(result)
	# print(shuffled)
	guessed  = player_guess()
	print(guessed)
	final_guess = check_guess(result,guessed)
	print(final_guess)
