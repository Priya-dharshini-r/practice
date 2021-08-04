'''
def pangram(string):
	alpha = "abcdefghijklmnopqrstuvwxyz"
	for char in alpha:
		if char not in string.lower():
			return False
	return True

op = pangram("the quick brown fox jumps over the lazy dog")
print(op)
'''
import string
alphabet = set(string.ascii_lowercase)
def pangram(string):
	# alphabet = set(string.ascii_lowercase)
	string = set(string.lower())
	return string >= alphabet
op = pangram("the quick brown fox jumps over the lazy dog")
print(op)
