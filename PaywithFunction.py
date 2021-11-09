while True:
    def computepay(hours, rate):
        if hours > 40:
            regular_pay = hours * rate
            overtime_pay = (hours - 40.0) * (rate * 0.5)
            total = regular_pay + overtime_pay
            print(total)

        else:
            total = hours * rate
            print(total)
            return total

    try:
        hours = input('Enter Hours\n')
        rate = input('Enter Rate\n')
        hours = int(hours)
        rate = float(rate)

        pay = computepay(hours, rate)
        print(pay)
    except:
        print('Enter Digits please')