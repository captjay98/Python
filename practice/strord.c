#!/usr/bin/python3


import code


x = input("Enter a string to hide in upper case :- ")
sec = ""

for i in x:
    sec += str(ord(i) - 23)
print("Sec = ", sec)

norm = ""

for c in range(0, len(sec) -1, 2):
    code = sec[c] + sec[c + 1]
    norm += chr(int(code) + 23)
print("Original Message = ", norm)




