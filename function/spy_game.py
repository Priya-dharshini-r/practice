def spy_game(game_list):
	spy_list = []
	for i in game_list:
		if i == 0 or i == 7:
			spy_list.append(i)
	# Spy list convert to string
	string = "".join(map(str,spy_list))
	print("String", string)
	return string == "007"

if __name__ == "__main__":
	sp = [1,7,2,0,4,5,0]
	print(spy_game(sp))
	sp1 = [1,2,4,0,0,7,5]
	print(spy_game(sp1))
	sp2 = [1,0,2,4,0,5,7]
	print(spy_game(sp2))
