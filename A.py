import re

file = open('C:\ppy\mbox.txt')

for line in file:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
