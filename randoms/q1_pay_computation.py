#!/usr/bin/python3

"""A program that computes employee pay based on hours worked"""

while True:
    h = int(input("Enter Hours: "))
    r = int(input("Enter Rate: "))

    def pay_compute(hours, rate):
        if hours > 40:
            normal_pay = hours * rate
            extra_pay = (hours - 40.0) * (rate * 0.5)
            pay = extra_pay + normal_pay
            return pay
        else:
            pay = hours * rate
            return pay

    answer = pay_compute(h, r)
    print(f"pay = {answer} \n")
