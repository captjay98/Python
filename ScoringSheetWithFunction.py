
# Keeping the scoring in a loop
while True:

    # To catch and handle abberations
    try:

        # A function to store the scores
        def computegrade(score):
            grade = score
            return grade

        score = float(input("Enter Score"))

        # The scores and grading
        if computegrade(score) > 100 or computegrade(score) < 0:
            print('enter a valid score')
        elif computegrade(score) >= 90:
            print('A')
        elif computegrade(score) >= 80:
            print('B')
        elif computegrade(score) >= 70:
            print('C')
        elif computegrade(score) >= 65:
            print('C')
        elif computegrade(score) >= 55:
            print('D')
        elif computegrade(score) <= 54:
            print('F')
        else:
            print('enter a valid score please')
    # Catching exceptions
    except ValueError:
        print('Please input digit')
