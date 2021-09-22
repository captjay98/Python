while True:
    try:

        temp = float(input('Please enter Temperature\n'))

        tempC = int((temp - 32.0) * 5.0 / 9.0)

        unit = input("Enter C or F")

        if unit.upper() == "C":

            if tempC >= 30:
                print(f"It is {tempC} in C")
                print("It's a hot day, Stay Hydrated")

            elif tempC >= 20:
                print(f"It is {tempC} in C")
                print("it's a nice day, Enjoy")

            elif tempC < 20:
                print(f"It is {tempC} in C")
                print("It's chilly today, Stay Warm")

            else:
                print("Check your input")

        else:
            unit.upper() == "F"

            if temp >= 88:
                print(f"It is {temp} in F")
                print("It's a hot day, Stay Hydrated")

            elif tempC >= 69:
                print(f"It is {temp} in F")
                print("it's a nice day, Enjoy")

            elif tempC < 69:
                print(f"It is {temp} in F")
                print("It's chilly today, Stay Warm")

            else:
                print("Check your input")

    except:
        print("This is a weather bot")
        quit()

