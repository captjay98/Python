#!/usr/bin/python3

def asc(char):

    return ("{:s}".format(chr(char)))


x = input("Enter Number")
x = int(x)
print(f" Ascii number {x} is {asc(x)}")
