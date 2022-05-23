import math

while True:

    num1 = input("Enter Num = ")
    num1 =float(num1)

    num2 = input("Enter num 2 = ")
    num2 = float(num2)

    answer = num1 // num2

    print(answer)

    digit = input('Enter Digits = ')
    digit = float(digit)

    sig = input('To what significant Number? =  ')
    sig = int(sig)

    result = round(digit, sig)
    
    print(result)








