#!/usr/bin/python3
"""calculates avrage grade in a class"""


def grade_compute(grades):
    total = 0
    for item in grades:
        total = total + item

    average = total / len(grades)
    print(f"Average of the class is {average}")

scores = [60, 70, 90, 40, 50]
grade_compute(scores)
