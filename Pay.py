while True:

    try:
        hours = input('Enter Hours\n')
        rate = input('Enter Rate\n')

        hours = int(hours)
        rate = float(rate)

        if hours > 40:
            pay = hours * rate
            overtime = (hours - 40.0) * (rate * 0.5)
            overtime_pay = pay + overtime
            print(overtime_pay)

        else:
            pay = hours * rate
            print(pay)
    except ValueError:
        print('Error, Please enter numeric input')
