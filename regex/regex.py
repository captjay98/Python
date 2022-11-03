#!/usr/bin/python3


import re

"""
reg = " I am Jamal Ibrahim Umar, Hello World! "

match = re.search(r'Jamal', reg)

print('Start Indx:', match.start())
print('End Index', match.end())
print(match)

^ matches beginning the begginning of the string
^Ja

$ matches end of the string
im$


. matches any char except newline
J.m*
.. contains atleast 2 char

| or
j|k

? zero or one occurenece
ji?

* any occurence
ja*al will match jamal
ja*l will not match


+ one or more occurence
ja+m will mach jamal
ja+l will not match


{} indicate number of occurences preceding regex to match
a{1-3}
will match thre 
() enclose a group of regex


# \ drop special meaning
str = " Jamal.Ibrahim "
match = re.search(r'\.', str)
print(match)


[0,3] any number from 1 to 3
[a-c] any letter from a to c
[^0,3] any number not including 1 to 3
[^a-c] any letter not including a to c


Special characters

\A matches if string starts with the char
\AJ
matches Jamal

\b matches if word begings or ends with the char

\bl
matches Jamal

\B string should not start with letter
\BJ
doesnt match Jamal


\d matches any digit

\D matches any non digit

\s matches whitespace

\S matches non whitespace

\w matches any alphanumeric

\W matches any non alphanumeric

\Z matches if string ends with

"""

str = "Hello im am jamal i live at cc95 my number is 095675566"

reg = '\d+'

match = re.findall(reg, str)
print("found" ,match)


rx = re.compile('\d+')

match = rx.findall(str)
print(match)


rx = re.compile('\w+')
print(rx.findall(str))
