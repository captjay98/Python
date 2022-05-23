rounds = input("Enter Number of Rounds :-")
rounds = int(rounds)

i = 1

while i <= rounds:
            
    num = input("Enter a Number :-")
    rem = int(num) % 2
    total = []
    tots = total.append(rem)
        
        
    if rem == 0:
        print("Number is Even")
        
    elif rem != 0:
        print("Number is  Odd")
            
    elif rem != 0 and rem != 1:
        print("Number is Prime")
        
    else:
        print("Invalid input")
            
