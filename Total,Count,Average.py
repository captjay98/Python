total = 0
count = 0
average = 0

while True:
    num = input('Enter a number \n')
    if num == 'done':
        break
    try:
        num = float(num)
    except:
        print('Invalid input')
        continue
    total = total + num
    count = count + 1
    average = total / count
print("Total", total , "Count" , count,  "Average", average)
