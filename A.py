import re

file = open('C:\ppy\mbox.txt')

for line in file:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

x = 'My 5 Favourite numbers are 98 and 0'
y = re.findall('[0-9]+', x)
print(y)

# Greedy
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

# Not Greedy
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)

# Extract Email
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)

# Extract Email
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)', x)
print(y)

# REMOVE HOST
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)', x)
print(y)

x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', x)
print(y)

# EXTRACTTION
file = open('C:\ppy\mbox.txt')
numlist = []
for line in file:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)
