PasswordFile = open('SecretPassword.txt')
SecretPassword = PasswordFile.read()
print('Enter Password')
TypedPassword = ()
if TypedPassword == SecretPassword:
    print('Access Granted')
    if TypedPassword == '12345':
        print('That Password is one that an idiot puts on their luggage.')
else:
    print('Access Denied')

import random
import sys

wins = 0
losses = 0
ties = 0
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your Move: (r)ock (p)aper (s)cissors or (q)uit')

        playerMove = input()
        if playerMove == 'q':
            sys.exit()

        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r, p, s, or q.')

    if playerMove == 'r':
        print('ROCK versus...')

    elif playerMove == 'p':
        print('PAPER versus...')

    elif playerMove == 's':
        print('SCISORS versus...')

    randonNumber = random.randint(1, 3)
    if randonNumber == 1:
        computerMove = 'r'
        print('ROCK')

    elif randonNumber == 2:
        computerMove = 'p'
        print('PAPER')

    elif randonNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    if playerMove == computerMove:
        print('it is a tie!')
        ties = ties + 1

    elif playerMove == 'r' and computerMove == 's':
        print('YOU WIN!')
        wins = wins + 1

    elif playerMove == 'p' and computerMove == 'r':
        print('You WIN!')
        wins = wins + 1

    elif playerMove == 's' and computerMove == 'p':
        print('You WIN!')
        wins = wins + 1

    elif playerMove == 'r' and computerMove == 'p':
        print('You Lose!')
        losses = losses + 1

    elif playerMove == 'p' and computerMove == 's':
        print('You Lose')
        losses = losses + 1

    elif playerMove == 's' and computerMove == 'r':
        print('You Lose')
        losses = losses + 1
