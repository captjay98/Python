# abcdefg
# page 31 chapter 2 VARIABLES, EXPRESSIONS AND STATEMENTS

# Values and Types
# str,int,float

# Variables
# and+ as assert break class continue def+
# del elif+ else+ except+ false+ finally for+
# from global if+ import+ in+ is+ lambda
# none nonlocal not+ or+ pass+ raise return
# true+ try+ while+ with yield async await

# Statements and Assignments

# Operands
# PEMDAS

import json
import xml.etree.ElementTree as ET
import ssl
from bs4 import BeautifulSoup
import urllib.error
import urllib.parse
import urllib.request
import socket
import re
import random
import math


def func():
    print('updated')


number1 = input('Input Number 1\n')
number2 = input('input Number 2\n')
number1 = int(number1)
number2 = int(number2)

multiplication = number1 * number2

division = number1 * number2

quotient = number1 // number2

remainder = number1 % number2

addition = number1 + number2

substitution = number1 + number2

exponentiation = number1 ** number2

print(multiplication)

print(division)

print(quotient)

print(remainder)

print(addition)

print(substitution)

print(exponentiation)


# input
# Most repeated word finder in beginning of book
name = input('enter file')
handle = open(name, 'r')
counts = dict()

count = 0
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = count.get(word, 0) + 1


bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        Bigcount = count

prompt = ' how old are you?\n'
age = input(prompt)
int(age) + 3
print(age)

# oe

age = input(' how old are you?\n')
age = int(age)
print(age + 2)

# Exercise 2.15

name = input('please enter your name\n')
print(name)

hours = input('Enter Hours\n')
hours = int(hours)

rate = input('Enter Rate\n')
rate = float(rate)

pay = (hours * rate)
print(pay)

width = 17
height = 12.0

print(width // 2)
print(width/2)
print(height/3)
1 + 2 + 5

patient_name = "John smith"
patient_age = 20
new_patient = True

birth_year = int(input("Enter Birth year:"))
age = 2021 - (birth_year)
print(age)

first_number = float(input("Enter First Number:"))

second_number = float(input("Enter Second Number:"))

sum = (first_number) + (second_number)

print(sum)

tempf = input('Please enter Temperature in C\n')
tempf = float(tempf)

tempc = (tempf - 32.0) * 5.0 / 9.0
print(tempc)

tempf = input('Please enter Temperature in F\n')

tempf = float(tempf)
tempc = (tempf - 32.0) * 5.0 / 9.0
print(tempc)

print('Please enter a number')

# CHAPTER 3 CONDITIONAL EXECUTION
# Boolean expressions
# x > y
# x < y
# x >= y
# x <= y
# x is y
# x is not y

# Logical operators
# and or not

# Conditional Operators

if 5 % 2 == 0:
    print('x is even')
else:
    print('x is odd')
if 1 > 0:
    print('positive')
if 1 > 0:
    pass
if 1 > 2:
    print('negative')

if 1 < 0:
    print('1 is less than 0')
elif 1 > 2:
    print('x is greater than y')
else:
    print('x and y are equal')

choice = input('enter letter\n')

if choice == 'a':
    print('Bad guess')
elif choice == 'b':
    print('Good guess')
elif choice == 'c':
    print('close, but not correct')

# EXERCISE 3.11
try:
    hours = input('Enter Hours\n')
    hours = int(hours)

    rate = input('Enter Rate\n')
    rate = float(rate)

    if hours > 40:
        pay = (hours * (rate + 0.5556))
        print(pay)

    else:
        pay = (hours * rate)
        print(pay)
except ValueError:
    print('Error, Please enter numeric input')


while True:
    try:
        def computegrade(score):
            grade = score
            return grade

        score = float(input("Enter Score"))

        if computegrade(score) > 1.0 or computegrade(score) < 0.0:
            print('Enter Score beteen 0 - 1.0')
        elif computegrade(score) >= 0.9:
            print('A')
        elif computegrade(score) >= 0.8:
            print('B')
        elif computegrade(score) >= 0.7:
            print('C')
        elif computegrade(score) > 0.6:
            print('D')
        elif computegrade(score) < 0.6:
            print('F')
        else:
            print('You be MUmU?')

    except ValueError:
        print('Please input digit')

while True:
    try:
        temperature = float(input('Please enter Temperature in F\n'))

        tempC = int((temperature - 32.0) * 5.0 / 9.0)
        print(f"It is {tempC} in C")

        if tempC >= 30:
            print("it's a hot day")
            print("Stay Hydrated")

        elif tempC >= 20:
            print("it's a nice day")

        elif tempC < 20:
            print("It's chilly today")

        else:
            print("Check your input")

        print('Have a good day')
    except ValueError:
        print("Enter Digits Please")

# def farenheit():
    # calc = float(input('Please enter Temperature in F\n'))
    # return calc


# def celsius():
    # cal = int((farenheit() - 32.0) * 5.0 / 9.0)
    # return cal

while True:
    try:
        temp = float(input('Please enter Temperature in F\n'))

        def farenheit():
            return temp

        def Celsius():
            tempc = int((temp - 32.0) * 5.0 / 9.0)
            return tempc

        unit = input("Enter Unit")

        if unit.upper() == "F":
            if farenheit() >= 88:
                print(f"It is {farenheit()} in F")
                print("it's a hot day, Stay Hydrated")

            elif farenheit() >= 69:
                print(f"It is {farenheit()} in F")
                print("it's a nice day")

            elif farenheit() < 69:
                print(f"It is {farenheit()} in F")
                print("It's chilly today, Stay Warm")

            else:
                print("Check your input")

        elif unit.upper() == "C":
            if Celsius() >= 30:
                print(f"It is {Celsius()} in C")
                print("it's a hot day, Stay Hydrated")

            elif Celsius() >= 20:
                print(f"It is {Celsius()} in C")
                print("it's a nice day, Enjoy")

            elif Celsius() < 20:
                print(f"It is {Celsius()} in C")
                print("It's chilly today, Stay Warm")

            else:
                print("Check your input")
        else:
            print('Enter C or F')

    except ValueError:
        print("Enter Digits Please")


def temp(a):
    cal = float(input('Please enter Temperature\n'))
    return cal


def tempC(a):
    calc = int((temp - 32.0) * 5.0 / 9.0)
    return calc

    if t >= 30:
        print("It is Hot Today")

    elif t >= 20:
        print("It's a Nice Day")

    elif t < 20:
        print("It is Cold Today")

    else:
        print("Check Input please")


while True:
    try:

        def farenheit(t):
            temp = t
            return temp

        t = int(input('Please enter Temperature in F\n'))

        def celsius():
            tempc = int((t - 32.0) * 5.0 / 9.0)
            return tempc

        unit = input("Enter Unit")

        if unit.upper() == "F":

            if farenheit(t) >= 88:
                print(f"It is {farenheit(t)} in F")
                print("it's a hot day, Stay Hydrated")

            elif farenheit(t) >= 69:
                print(f"It is {farenheit(t)} in F")
                print("it's a nice day")

            elif farenheit(t) < 69:
                print(f"It is {farenheit(t)} in F")
                print("It's chilly today, Stay Warm")

            else:
                print("Check your input")

        elif unit.upper() == "C":
            if celsius() >= 30:
                print(f"It is {celsius()} in C")
                print("it's a hot day, Stay Hydrated")

            elif celsius() >= 20:
                print(f"It is {celsius()} in C")
                print("it's a nice day, Enjoy")

            elif celsius() < 20:
                print(f"It is {celsius()} in C")
                print("It's chilly today, Stay Warm")

            else:
                print("Check your input")
        else:
            print('Enter C or F')

    except ValueError:
        print("Enter Digits Please")

weight = float(input("Please input weight \n"))
unit = input("(K)g or (L)bs \n")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs" + str(converted))

if unit.upper() == "L":
    converted = weight * 0.45
    print("Weight in Kgs:" + str(converted))
else:
    print("Enter either K or L")
# CHAPTER 4 FUNCTIONS
# max, min, len,
# import math
# math.log10(ratio)
# math.sin(radians)
# math.sqrt()
# math.poow(2 numbers base and exponent)


degrees = 45
radians = degrees / 360.0 * 2 * math.pi


math.sin(radians)

signal_power = 0
noise_power = 0
ratio = signal_power/noise_power
decibels = 10 * math.log10(ratio)

# Exercise

for i in range(10):
    x = random.random()
    print(x)

random.radint(5, 10)

t = [1, 2, 3]
random.choice(t)

# Adding New Functions


def Fav_lyrics():
    print("Will Never love a'gain")
    print('The way i loved you.')


print(Fav_lyrics())


def rep_fav():
    Fav_lyrics()
    Fav_lyrics()


print(rep_fav())


def print_twice():
    print(math.pi)
    print('math.pi')


print_twice()


def print_name_twice():
    print("jamal")
    print('jamal')


print_name_twice()


def print_twice(Jamal):
    print(Jamal)
    print(Jamal)


print_twice('Jamal ' * 4)  # Fruitful function

print_twice('spam' * 4)

print_twice(math.cos(math.pi))

kal = 'golon, yaro.'
print_twice(kal)


# print_twice() #Void Function

# Value None is not the same as string None

def jointwo(a, b):
    joined = a + b
    return joined


x = jointwo(int(input('Enter Digits')), int(input('Enter Digits')))
print(x)


def fred():
    print("ZAP")


def jane():
    print('ABC')


jane()
fred()
jane()


def greet(lang):
    if lang == "es":
        return('Hola')
    elif lang == "fr":
        return'Bonsoir'
    else:
        print('Hello. World!')


print(greet("es"), "Jamal")


def greeting():
    return 'Hello'


print(greet("fr"), "Jamal")

print(greeting(), "Jamal")


def addition(a, b):
    added = a + b
    return added


test = addition(int(input('Enter Digits')), int(input('Enter Digits')))
print(test)

test = addition(5, 5)
print(test)

# EXERCISE 4.14
while True:
    try:
        hours = input('Enter Hours\n')
        hours = int(hours)

        rate = input('Enter Rate\n')
        rate = float(rate)

        def computepay(a, b):
            pay = hours * rate
            return pay

        if hours > 40:
            print(computepay() * 1.057)

        if hours <= 40:
            print(computepay())

    except ValueError:
        print('Error, Please enter numeric input')


# CHAMPTER 5 ITERATION

# While statements

i = 1
while i <= 12:
    print(i * '*')
    i = i + 1

j = 12
while j > 0:
    j = j - 1
    print(j * '*')

n = 1
while n < 2021 - 1998:
    print(f"Jamal is getting older\n{n} ")
    n = n + 1
print(f"He's now {n} years old")

while True:
    data = input('Enter Data \n')
    if data == 'This is the Data':
        break
    print(data)

print("Here's the correct data")

J = 22
while J > 0:
    print(J)
    J = J - 1
print('Boom Shakalaka')

# Finishing iterations with continue
while True:
    data = input('Enter Data \n')
    if data[0] == "#":
        continue
    if data == 'Data1':
        break
    print(data)
print("Here's the correct data")

# For loops
numbers = [1, 2, 3, 4, 5, ]
for number in numbers:
    print(numbers)

# Definite loops using for
friends = ['Ace', 'Bsal', 'Bib', 'Kal']
for friend in friends:
    print('Wassup', friend)


clients = ['ASD', 'BSD', 'CSD', 'DSD', 'ESD', 'FSD', 'GSD']
for client in clients:
    print('Thank you for your patronage', client)
print('Success')

# Largest
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)

# Smalllest
smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)

# Counting
count = 0
print('before', count)
for num in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    print(count, num)
print('After', count)

# sum
count = 0
print('Before', count)
for thing in [9, 41, 12, 3, 74, 15]:
    count = count + thing
    print(count, thing)
print('After', count)

# sum & Count
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)

# Largest
print('Before')
for digit in [9, 41, 12, 3, 74, 15]:
    if digit > 20:
        print('Large Number', digit)
print('Done')

# Finding
found = False
print('Before', found)
for bool in [9, 41, 12, 3, 74, 15]:
    if bool == 3:
        found = True
    print(found, bool)
print('After', found)

# LEN
clients = 0
for client in [3, 41, 12, 9, 74, 15]:
    clients = clients + 1
print('Clients: ', clients)

# SUM
total = 0
for num in [3, 41, 12, 9, 74, 15]:
    total = total + num
print('Total: ', total)

total = 0
inp = (input('Enter Digits'))
num = inp.split()
print(num)
for numb in num:
    total = total + int(numb)
print(total)

# Saving my Ass
input_string = input('Enter Digits')
print('\n')
user_list = input_string.split()

print('list: ', user_list)

for i in range(len(user_list)):

    user_list[i] = int(user_list[i])
print('sum =', sum(user_list))

# MAX
Largest = None
print('Before:', Largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if Largest is None or itervar > Largest:
        Largest = itervar
    print('Loop:', itervar, Largest)
print('Largest:',  Largest)

# MIN
smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)


def min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest

# EXERCISE 5.9


num = 0
total = 0
count = 0
average = 0

while True:
    num = input('Enter a number \n')
    if num == 'done':
        break
    try:
        float(num)
    except ValueError:
        print('Invalid input')
    continue
    total = total + float(num)
    count = count + 1
    average = total / count

print("Total", total,  "Count", count,  "Average", average)

# A BETTER WAY
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


while True:
    num = int(input('Enter a number \n'))
    if num == 'done':
        break
    print(num)

for numb in num:
    total = num + numb
    print('Numb: ', numb)

for numb in num:
    total = total + numb
    print('Numb: ', numb)

num = input()
numbers = num.split()
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

num = list()
while True:
    inp = input('Enter Numbers')
    if inp == 'done':
        break
    value = int(inp)
    num.append(value)

print(sum(num), len(num))
print(num[0])


print(type(numbers))

numbers = range(5, 10, 2)
for number in numbers:
    print(number)

while True:
    line = input(">")
    if line.startswith == '#':
        continue
    if line == 'done':
        break
    print(line)
print('DOne!')


i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)

# STRINGS

# SLICES
fruit = "banana"

print(len(fruit))

print(fruit[-2])

# String Traversal
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

# Better option
for char in fruit:
    print(char)

for letter in 'banana':
    print(letter)

# Number of letters
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


# String slices

s = 'monty python'
print(s[0:5])
print(s[6:12])

print(fruit[:3])
print(fruit[3:])

s = 'Python  Guru'
print(s[0:6])
print(s[8:12])
print(s[:6])
print(s[8:])

fruit = "banana"
print(fruit[:])

example = "WADUP, DAWG?"
new_example = 'WAS' + example[3:]
print(example)
print(new_example)


title = "Python Automation Guru"
# 0123456789
print(title.upper())
print(title.lower())
print(title.find('i'))
print(title.replace('Guru', 'Enthusiast'))
print(title)
print('Guru' in title)


# Strings are immutable
fruit = 'banana'
greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)


# The in operator/Looping and Counting
fruit = 'banana'
print('a' in fruit)

x = 'n' in fruit
print(x)

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


def countLetters(str, let):
    content = str
    count = 0
    for letter in content:
        if letter == let:
            count = count + 1
    print(count)


print(countLetters('bananaaaaaaaa', 'a'))

# Counter function


def counter(s, let):
    string = str(s)
    letter = str(let)
    count = 0
    for alpha in string:
        if alpha == letter:
            count = count + 1
    print(count)


print(counter('banana', 'a'))

# String Comparison
word = 'banana'
if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word,' + word + ' ,  comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

# Strings methods/parsing strings

print('Hi There' .lower())
word = 'banana'
new_word = word.upper()
print(new_word)

word = 'banana'
index = word.find('na', 4)
print(index)

print('Hi There'.lower())
greet = 'Hello Kal'
greeet = greet.replace('Kal', 'Bib')
print(greet)
print(greeet)
test = greeet.replace('o', 'x')
print(test)

line = '  Here we go  '
line.lstrip()
line.rstrip()
line.strip()

line = 'Have a nice day'
line.startswith('Have')
line.lower()
line.lower().startswith('h')

data = 'From stephen.marquard@ uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find('', atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)

# Format operator
camels = 42
'%d' % camels
print('i have spoted %d camels.' % camels)


# exercise 6.14
data = 'X-DSPAM-Confidence:0.8475'
atpos = data.find('0')
print(atpos)
print(data[19:25])
float(0.8475)

data = 'X-DSPAM-Confidence:0.8475'
firstpos = data.find('0')

extracted = data[firstpos:]
slice = float(extracted)

print(slice)
print(type(slice))

# Restart and understand everything

# FILES
stuff = 'Hello \nWorld '
stufff = 'X\nY'
print(len(stufff))
print(stuff)

#  File
file = open("Enter File")  # "C:\ppy\mbox.txt"

# Counting File lines
count = 0
for line in file:
    count = count + 1
print('Line Count:', count)

# Len of file
inp = file.read()
print(len(inp))

print(inp[:6687005])

# Finding Startswith and striping
for line in file:
    if line.startswith(('From:')):
        line = line.strip()
        print(line)


for line in file:
    line = line.strip()
    if not line.startswith(('From:')):
        continue
    print(line)


for line in file:
    line = line.strip()
    if '@uct.ac.za' not in line:
        continue
    print(line)

# Using inputs
f = input('Enter file name: \n')  # "C:\ppy\mbox.txt"
file = open(f)
count = 0
for line in file:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'Subject lins in', file)

# Catching Exceptions
f = input('Enter file name: ')  # "C:\ppy\mbox.txt"
try:
    file = open(f)

    count = 0
    for line in file:
        if line.startswith('Subject:'):
            count = count + 1
    print('There were', count, 'Subject lines in', file)
except ValueError:
    print('Invalid File:', f)

# Writing Files
fout = open('output.txt', 'w')
print(fout)

line1 = "This here's the wattle, \n"
print(fout.write(line1))

line2 = 'the emble of our land. \n'
fout.write(line2)
print(line2)

fout.close


for line in file:
    line = line.strip()
    if line.startswith('X-DSPAM-Confidence:'):
        print(line.find(0))
# except:
    print('Invalid File:', f)

# EXERCISE

f = input('Enter file \n')  # "C:\ppy\mbox.txt"
file = open(f)
for line in file:
    line = line.strip()
    line = line.upper()
    print(line[:50])


f = input('Enter file ')  # "C:\ppy\mbox.txt"
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


while True:
    try:
        s = input("What?")

        if s == ("I Love You Python"):
            print('I Love You Too Capt Jay')
            break

        else:
            ("I don't know what you're saying")

    except ValueError:
        print("You're not serious")


# Lists

names = ["Kal", "Sal", "Bal", "Dal"]
names[0] = "kall"
print(names[0:0])
print(names)


numbers = list()
numbers.append(6)
numbers.append(5)
numbers.append(9)
numbers.append(8)
numbers.append(2)
numbers.insert(0, -1)
numbers.remove(6)
print(numbers)
print(7 in numbers)
print(7 not in numbers)
print(len(numbers))
print(sum(numbers))
numbers.sort()
print(numbers)
print(sum(numbers)/len(numbers))


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a)

t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])
numbers = (1, 2, 3, 3)
print(numbers.count(3))


total = 0
count = 0
while True:
    inp = input('Enter Number')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print(average)

numlist = list()
while True:
    inp = input('Enter Number')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print(average)

abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))

for thingy in stuff:
    print(thingy)

de = 'With;three;words'
thing = de.split()
print(thing)

thing = de.split(';')
print(thing)

f = input('Enter file name: \n')  # "C:\ppy\mbox.txt"
file = open(f)
for line in file:
    line = line.rstrip()
    if not line.startswith('From '):
        continue

    words = line.split()
    print(words[2])

    email = words[1]
    print(email)

    pieces = email.split('@')
    print(pieces[1])


f = input('Enter file name: \n')  # "C:\ppy\mbox.txt"
file = open(f)

for line in file:
    line = line.rstrip()
    wds = line.split()

    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])


# DICTIONARIES
store = {}
store['Tires'] = 2
store['Rims'] = 5
store['nuts'] = 57
print(store)
print(store['nuts'])
store['nuts'] = store['nuts'] + 3
print(store)

dic = dict()
dic['Age'] = 22
dic['Course'] = 'CS'
print(dic)
dic['Age'] = 23
print(dic)

counts = {}
names = ["Kal", "Sal", "Bal", "Dal", "Kal", "Bal", "Kal", "Sal", "Kal", "Bal"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

x = counts.get(name, 0)
print(x)

counts = dict()
names = ["Kal", "Sal", "Bal", "Dal", "Kal", "Bal",
         "Kal", "Sal", "Bal", "Dal", "Kal", "Bal"]
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)


#
counts = dict()
text = input("Enter Text :")
# "the clown ran after the car and the car ran into the tent the and the ten
# fell down on the clown and the")
words = text.split()

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)


counts = {'Name': 'Jamal', 'Age': 22, 'Height': 183}
for key in counts:
    print(key, counts[key])


anew = {'Name': 'Jamal', 'Age': 22, 'Height': 183}
print(list(anew))

print(anew.keys())

print(anew.values())

print(anew.items())

for key, value in anew.items():
    print(key, value)


# EXERCISE

dic = {}
for line in handle:
    line = line.rstrip()
    words = line.split()

    for word in words:
        # If key is not there count is Zero
        oldcount = dic.get(word, 0)
        print(word, 'old', oldcount)

        newcount = oldcount + 1
        dic[word] = newcount
        print(word, 'new', newcount)

        if word in dic:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1

print(dic)


file = input('Enter File: ')
if len(file) < 1:
    file = 'C:\ppy\intro.txt'

handle = open(file)

dic = {}
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        dic[word] = dic.get(word, 0) + 1
        print(word, 'new', dic[word])
# print(dic)

largest = -1
theword = None
for key, value in dic.items():
    print(key, value)
    if value > largest:
        largest = value
        theword = key
print('Done', theword, '--', largest)

# Tuples

(Name, Age) = ('Jamal', 23)

print(Name, Age)

dic = {}
dic['name'] = 'Jamal'
dic['age'] = 98

for (key, value) in dic.items():
    print(key, value)

tups = dic.items()
print(tups)

# only looks at the first value when comparing
(5, 6, 7) > (6, 7)

('j', 'k') > ('a', 'b')

tools = {'cox': 9, 'box': 7, 'axe': 5}
print(tools.items())
print(sorted(tools.items()))

for (key, value) in sorted(tools.items()):
    print(key, value)

tem = list()
for key, value in tools.items():
    tem.append((value, key))
print(tem)
tem = sorted(tem, reverse=False)
print(tem)


(Name, Age) = ('Jamal', 23)

print(Name, Age)

dic = {}
dic['name'] = 'Jamal'
dic['age'] = 98

for (key, value) in dic.items():
    print(key, value)

tups = dic.items()
print(tups)

(5, 6, 7)

file = open("C:\ppy\intro.txt")
counts = {}
for line in file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = []
for key, value in counts.items():
    newtuple = (value, key)
    lst.append(newtuple)

lst = sorted(lst, reverse=True)

for value, key in lst[:10]:
    print(key, value)

tools = {'cox': 9, 'box': 7, 'axe': 5}

print(sorted([(value, key) for key, value in tools.items()]))

# Regular Expressions


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

# More extraction
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)

# Networked Programs

# Sockets


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

# urllib

file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in file:
    print(line.decode().strip())


file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in file:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter url==')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter url==')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

# xml


data = '''

<person>
<name>Jamal</name>
<phone type="init">
  +2348137443466
</phone>
<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))


input = '''

<stuff>
  <users>
    <user x="5">
       <id>008</id>
       <name>Jay</name>
    </user>
    <user x="6">
       <id>009</id>
       <name>CAP</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User Count', len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute:', item.get("x"))


# Json


data = '''{"name" : "Jamal",
"phone" : {
  "type" : "intl",
  "number" : "+2348137443466"
  },
"email" : {
  "hide" : "yes"
  }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('hide:', info["email"]["hide"])


data = '''[
{"id" : "98",
  "x" :"5",
  "name" : "Jamal"},
{"id" : "67",
  "x" : "6",
  "name" : "Ibrahim"
  }]'''

info = json.loads(data)
print('User Count:', len(info))
for item in info:
    print('Name:', item['name'])
    print('id:', item["id"])
    print('Attribute', item['x'])

# GEOJSON


serviceurl = 'http://maps.googleapis.com/api/geocode/json?'

while True:
    address = input('Enter location:')
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    ur = urllib.request.urlopen(url)
    data = ur.read().decode()
    print('Retrived', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== fAILURE TO RETIVE ===')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, "lng", lng)
    location = js['results'][0]['formatted_address']
    print(location)

OOP


class Human:

    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "Tennis":
            print(self.name, "Play's Tennis")
        elif self.occupation == "Actor":
            print(self.name, "Makes Movies")

    def speaks(self):
        print(self.name, "Speaks English")


tom = Human("Tom Cruise", "Actor")
tom.do_work()
tom.speaks()

maria = Human('Maria Sharapova', "Tennis")
maria.do_work()
maria.speaks()

print(type(Human))
print(dir(Human))

class Human:

    def __init__(self, name, age, occupation, height, weight, complexion):
        self.name = name
        self.occupation = occupation
        self.age = age
        self.height = height
        self.weight = weight
        self.complexion = complexion

    def likes(self):
        if self.name == "Jamal":
            print(self.name, "Plays Xbox games alot")
        elif self.name == "random":
            print(self.name, "does what humans do")

    def speaks(self):
        print(self.name, "Speaks English")

    def loves(self):
        if self.occupation == "Programmer":
            print(self.name, "Loves Python")
        elif self.occupation == "Graduate":
            print(self.name, "Just doing regular work")


me = Human("Jamal", 23, "Programmer", 180, 65, 'dark')
me.likes()
me.loves()
me.speaks()
# Get customers name
# Get order Date
# Get delivery date
# Get amount paid if*
# Customer Address
# Delivery Details
# Reminder 24 and 12 hours to
# Inventory list

# Building a Kalbot

client_name = input(
    'Hello, This is the Kalbot, May i Know your name please?\n')

print('Welcome to Kalbites', client_name)

print("What would you like to order today?  \n")
print("Kindly select a corresponding Number from the Menu below,Thank You \n.")

print("1. Cake \n2. Parfait \n3. Tres leches \n4. Brownie \n5. Milkshake \n")

menu = input(["blank", "1. Cake ", "2. Parfait",
              "3. Tres leches", "4. Brownie", "5. Milkshake"])
print(type(menu))
