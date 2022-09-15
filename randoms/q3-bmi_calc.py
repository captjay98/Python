#!/usr/bin/python3
"""Program that calculates bmi"""

def bmi_compute(weight, height):
    bmi = weight / (height / 100) **2
    return bmi

w = float(input("Enter Weight: "))
h = float(input("Enter Height: "))

bmi = bmi_compute(w, h)
print(bmi, "\n")


if bmi <= 18.4:
    print( "You are Underweight.")
elif bmi <= 24.9:
    print("You are Healthy.")
elif bmi <= 29.8:
    print("You are overweight.")
elif bmi <= 34.9:
    print("You are severely overweight.")
elif bmi <= 39.9:
    print("You are obese.")
else:
    print("Error")
