f = input('Enter file  C:\ppy\mbox.txt \n')
file = open(f)

count = 0
total = 0
for line in file:
    line = line.strip()
    if line.startswith('X-DSPAM-Confidence:'):
        pos = line.find('0')
        extraction = line[pos:]
        spam = float(extraction)
        count = count + 1
        total = total + spam


print('There are', count, 'lines')
print('Spam Confidence Average is', total/count)



f = input('Enter file  C:\ppy\mbox.txt \n')
file = open(f)


spam = list()
for line in file:
    line = line.strip()
    if line.startswith('X-DSPAM-Confidence:'):
        pos = line.find('0')
        extraction = line[pos:]
        value = float(extraction)
        spam.append(value)

average = sum(spam) / len(spam)
print('There are', count, 'lines')
print('Spam Confidence Average is', average)





