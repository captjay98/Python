#!/usr/bin/python3

string = "Random access Memory"
string = string.upper()

string = string.split(" ")

for item in string:
    print(item[0], end="")


