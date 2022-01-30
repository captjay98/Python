s = input ('enter score between 0-100\n')
s = float(s)

def computegrade():
    grade = s
    return s
if s > 100 or s < 0.0:
   print('enter a valid score')
elif s>=90:
    print('A')
elif s>=80:
    print('B')
elif s>=70:
    print('C')
elif s>60:
    print('D')
elif s<60:
    print('F')
else:
    print('enter a valid score please')
