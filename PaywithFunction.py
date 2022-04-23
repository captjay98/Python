while True:
    def computepay(hours, rate):
        if hours > 40:
            regular_pay = hours * rate
            overtime_pay = (hours - 40.0) * (rate * 0.5)
            pay = regular_pay + overtime_pay
        else:
            pay = hours * rate
        return pay

    try:
        hours = input('Enter Hours\n')
        rate = input('Enter Rate\n')

        hours = int(hours)
        rate = float(rate)

        pay = computepay(hours, rate)
        print("Pay = ", pay)

    except ValueError:
        print('Enter Digits Please')
