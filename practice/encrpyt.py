#!/usr/bin/python3

from curses.ascii import isupper


message = input("Enter message to encrypt \n")

key = int(input("Enter Number of shifts :-"))

sec_message = ""

for char in message:

    if char.isalpha():
        code = ord(char)
        code += key

        if char.isupper():

            if code > ord('Z'):
                code -= 26
            if code < ord('A'):
                code += 26

        else:
            if code > ord("z"):
                code -= 26
            if code < ord("a"):
                code += 26

        sec_message += chr(code)

    else:
        sec_message += char

print("Encrypted Key = ", sec_message)

key = -key
ori_message = ""

for char in sec_message:

    if char.isalpha():
        code = ord(char)
        code += key

        if char.isupper():

            if code > ord('Z'):
                code -= 26
            if code < ord('A'):
                code += 26

        else:
            if code > ord("z"):
                code -= 26
            if code < ord("a"):
                code += 26

        ori_message += chr(code)

    else:
        ori_message += char


print("Decrypted Key = ", ori_message)
