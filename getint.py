#!/usr/bin/python3

def getInt(message):
    while True:
        try:
            print("")
            choice = int(input(message))
            
        except ValueError:
            print("Enter a Digit you Bloody Idiat")
            continue

        else:
            return choice

choice = getInt("Enter a Number:-")
print(choice)
