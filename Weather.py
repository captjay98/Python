while True:
    try:

        def farenheit(t):
            temp = t
            return temp

        t = int(input('Please enter Temperature in F\n'))

        def celsius():
            tempc = int((t - 32.0) * 5.0 / 9.0)
            return tempc

        unit = input("Enter Unit")

        if unit.upper() == "F":

            if farenheit(t) >= 88:
                print(f"It is {farenheit(t)} in F")
                print("it's a hot day, Stay Hydrated")

            elif farenheit(t) >= 69:
                print(f"It is {farenheit(t)} in F")
                print("it's a nice day")

            elif farenheit(t) < 69:
                print(f"It is {farenheit(t)} in F")
                print("It's chilly today, Stay Warm")

            else:
                print("Check your input")

        elif unit.upper() == "C":
            if celsius() >= 30:
                print(f"It is {celsius()} in C")
                print("it's a hot day, Stay Hydrated")

            elif celsius() >= 20:
                print(f"It is {celsius()} in C")
                print("it's a nice day, Enjoy")

            elif celsius() < 20:
                print(f"It is {celsius()} in C")
                print("It's chilly today, Stay Warm")

            else:
                print("Check your input")
        else:
            print('Enter C or F')

    except ValueError:

        if (tempCF >= 88)
		{
			printf("It is %d in Farenheit\n", tempCF);
		    printf("It's a Hot Day, Stay Hydrated");
		}
		else if (tempCF >= 69)
		{
		    printf("It is %d in Farenheit\n", tempCF);
			printf("It's a Nice Day, Enjoy!");
		}
		else if (tempCF < 69)
		{
		    printf("It is %d in Farenheit\n", tempCF);
			printf("It is chilly Today, Stay Warm!");
		}        print("Enter Digits Please")
