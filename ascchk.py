#!/usr/bin/python3

def asc(char):

    return ("{:s}".format(chr(char)))

while True:
    x = input("Enter Number:-")
    x = int(x)

    if x < 0 or x > 150:
         print(f"{x} is out of range")

    else:
        print(f" Ascii number {x} is {asc(x)}")
