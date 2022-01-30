def countLetters(str, let):
    content = str
    count = 0
    for letter in content:
        if letter == let:
            count = count + 1
    return count


var = countLetters(input('Enter Word \n'), input('Enter letter \n'))

print(var)

def counter(s, l):
	string = str(s)
	letter = str(l)
	count = 0
	for alpha in string:
		if alpha == letter:
			count = count + 1
	print(count)


print(counter('banana', 'a'))
