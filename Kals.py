while True:
  try:
    hours = input('Enter Hours\n')
    hours = int(hours)

    rate = input('Enter Rate\n')
    rate = float(rate)

    def computepay():
        pay = hours * rate
        return pay
    print(computepay)

    if hours > 40:
       print (int(computepay() * 1.057))

    if hours <= 40:
       print(computepay())
  except:
    print('Error, Please enter numeric input')

