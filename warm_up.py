def display_list(game_list):
	print("Welcome to the Game, Let's go")
	print(game_list)

def user_input():
	value = 'not a digit'
	wrong_input = False
	acceptable_range = range(0,4)
	while value.isdigit() == False or wrong_input == False:
		value = input("Enter a number from (0-9): ")
		if value.isdigit() == False:
			print("Oops! This is not a number")
		if value.isdigit() == True:
			if int(value) in acceptable_range:
				wrong_input = True
			else:
				wrong_input = False
	return int(value)

def replacement_choice(gl, position):
	change = input("Enter the string to be in a position: ")
	gl[position] = change
	return gl


def continue_game():
	choice = 'just a check'
	while choice not in ['Y','N']:
		choice = input("If you want to play again type 'Y' or 'N':")
		if choice not in ['Y','N']:
			print("Please make a valid choice")
	if choice == 'Y':
		return True
	else:
		return False


if __name__ == "__main__":
	game_on = True
	gl = [0,1,2]
	while game_on:
		display_list(gl)
		position = user_input()
		print("Input:", position)
		gl = replacement_choice(gl,position)
		display_list(gl)
		game_on = continue_game()
