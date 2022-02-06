while True:
    try:
        def collatz(nunber):
            if nunber % 2 == 0:
                print('EVEN')
                print(nunber // 2)

            elif nunber % 2 == 1:
                print('ODD')
                print(3 * nunber + 1)

            return nunber

        nunber = collatz(int(input('Enter nunber:')))

    except ValueError:
        print('Enter digits only')
