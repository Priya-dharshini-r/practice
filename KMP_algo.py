# Knuth Morris and pratt algorithm to find if there is a pattern in given text.

'''
Step-1: Find an LPS(Longest purpose prefix which is also suffix)

--> Working of LPS:
	1. Create an 1D array with the size of the given pattern.
		LPS = []*len(Pattern)
	2. Set LPS[0] = 0
	3. Have two variable for iteration i and j respectively.
		i = 0, j = 1
	4. Check for pattern[i], Pattern[j] if both are same, set
		LPS[j] = i+1
		i = i+1, j = j+1
			Again back to step - 3
	5. If pattern[i] and pattern[j] is not matched,
		check for i, if i == 0
			LPS[j] = 0
			j = j+1 # Don't increment j.
		if i != 0,
			i = LPS[i-1]
			back to step - 3
	6. Repeat untill all the values in the LSP is Filled.

'''


