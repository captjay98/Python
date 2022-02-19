
num = list()
while True:
    inp = input('Enter a number \n')
    if inp == 'done':
        break
    try:
        value = float(inp)
        num.append(value)
    except ValueError:
        print('Please check your input')

print("Total", sum(num),  "Count", len(num),  "Average", sum(num)/len(num))
