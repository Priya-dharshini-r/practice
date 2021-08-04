def anagram(s, t):
	if sorted(s) == sorted(t):
		return True


op = anagram("anagram", "nagaram")
print(op)
