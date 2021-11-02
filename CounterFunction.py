def countLetters(str, l):
	content = str
	count = 0
	for letter in content:
		if letter == l:
			count = count + 1
	print(count)
print(countLetters('bananaaaaaaaa', 'a'))

#Counter function
def counter(s, l):
	string = str(s)
	letter = str(l)
	count = 0
	for alpha in string:
		if alpha == letter:
			count = count + 1
	print(count)
print(counter('banana', 'a'))