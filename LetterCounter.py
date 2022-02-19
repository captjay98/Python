def counter(s, let):
    string = str(s)
    letter = str(let)
    count = 0
    for alpha in string:
        if alpha == letter:
            count = count + 1
    return count


var = counter(input('Enter Word Please \n'), input('Enter Letter Please \n'))
print(var)
