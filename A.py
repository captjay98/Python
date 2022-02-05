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
