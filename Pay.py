try:
    hours = input('Enter Hours\n')
    hours = int(hours)

    rate = input('Enter Rate\n')
    rate = float(rate)

    if hours > 40:
        pay = (hours * (rate + 0.5556))
        print(pay)

    else:
        pay = (hours * rate)
        print(pay)
except:
    print('Error, Please enter numeric input')