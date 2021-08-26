#abcdefg
#page 31 chapter 2 VARIABLES, EXPRESSIONS AND STATEMENTS

#Values and Types
#str,int,float

#Variables
#and+ as assert break class continue def+
#del elif+ else+ except+ false+ finally for+
#from global if+ import+ in+ is+ lambda
#none nonlocal not+ or+ pass+ raise return
#true+ try+ while+ with yield async await

#Statements and Assignments

#Operands
#PEMDAS

def func():
    print('updated')
number1=input('Input Number 1\n')
number2=input('input Number 2\n')
number1=int(number1)
number2=int(number2)

multiplication= number1 * number2

division= number1 * number2

quotient= number1 // number2

remainder= number1 % number2

addition= number1 + number2

substitution= number1 + number2

exponentiation= number1 ** number2

print(multiplication)

print(division)

print(quotient)

print(remainder)

print(addition)

print(substitution)

print(exponentiation)



#input
#Most repeated word finder in beginning of book
name = input('enter file')
handle = open(name, 'r')
counts = dict()


for line in handle:
    words = line.split()
    for word in words:
        counts[word] = count.get(word, 0) + 1


bigcount = None
bigword  = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        Bigcount = count

prompt = ' how old are you?\n'
age = input(prompt)
int(age) + 3
print(age)

#oe

age= input(' how old are you?\n')
age = int(age)
print(age + 2)

#Exercise 2.15

name = input('please enter your name\n')
print(name)

hours =input('Enter Hours\n')
hours = int(hours)

rate = input('Enter Rate\n')
rate =  float(rate)

pay = (hours * rate)
print(pay)

width = 17
height = 12.0

print(width // 2)
print(width/2)
print(height/3)
1 + 2 + 5

atient_name = "John smith"
patient_age = 20
new_patient = True

birth_year = int(input("Enter Birth year:"))
age = 2021 - (birth_year)
print(age)

first_number = float(input("Enter First Number:"))

second_number =float(input("Enter Second Number:"))

sum = (first_number) + (second_number)

print(sum)

tempf= input('Please enter Temperature in C\n')
tempf = float(tempf)

tempc = (tempf - 32.0) * 5.0 / 9.0
print(tempc)

tempf= input('Please enter Temperature in F\n')

try:
    tempf = float(tempf)

    tempc = (tempf - 32.0) * 5.0 / 9.0
    print(tempc)
except:
    print('Please enter a number')

#CHAPTER 3 CONDITIONAL EXECUTION
#Boolean expressions
# x > y
# x < y
# x >= y
# x <= y
# x is y
# x is not y

# Logical operators
# and or not

# Conditional Operators

if 5%2 == 0 :
    print ('x is even')
else :
    print('x is odd')
if 1 > 0:
    print('positive')
if 1> 0 :
    pass
if 1 > 2:
    print('negative')

if  1 < 0:
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

#EXWERCISE 3.11
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
except:
    print('Error, Please enter numeric input')


while True:
 try:
   s = input('enter score between 0.0-1.0\n')
   s = float(s)

   def computegrade():
    grade = s
    return s
   if s > 1.0 or s < 0.0:
      print ('enter a valid score')
   elif s>=0.9:
      print('A')
   elif s>=0.8:
      print('B')
   elif s>=0.7:
      print('C')
   elif s>0.6:
      print('D')
   elif s<0.6:
      print('F')
   else:
      print('enter a valid score please')
 except:
   print('Please input digit')

   temperature = float(input("Please Enter Temperature"))

   if temperature > 30:
       print("it's a hot day")
       print("Stay Hydrated")
   elif temperature > 20:
       print("it's a nice day")
   elif temperature < 20:
       print("It's chilly today")
   else:
       print("Check your input")
   print('Have a good day')


weight = float(input("Please input weight \n"))
unit= input("(K)g or (L)bs \n")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs" + str(converted))

if unit.upper() == "L":
    converted = weight * 0.45
    print("Weight in Kgs:" + str(converted))
else:
    print("Enter either K or L")
#CHAPTER 4 FUNCTIONS
#max, min, len,
#import math
#math.log10(ratio)
#math.sin(radians)
#math.sqrt()
#math.poow(2 numbers base and exponent)

import math
degrees = 45
radians = degrees / 360.0 * 2 * math.pi
math.sin(radians)

#Exercise
import random

for i in range(10):
    x = random.random()
    print(x)

random.radint(5,10)

t = [1,2,3]
random.choice(t)

#Adding New Functions

def Fav_lyrics():
    print("Will Never love a'gain")
    print('The way i loved you.')
print(Fav_lyrics())


def rep_fav():
    Fav_lyrics()
    Fav_lyrics()

print(rep_fav())

import math


def print_twice():
    print(math.pi)
    print('math.pi')


print_twice()


def print_name_twice():
    print("jamal")
    print('jamal')


print_name_twice()

import math

def print_twice(Jamal):
    print(Jamal)
    print(Jamal)

print_twice('Jamal ' *4)  #Fruitful function

print_twice('spam' *4)

print_twice(math.cos(math.pi))

kal = 'golon, yaro.'
print_twice(kal)


#print_twice() #Void Function

#Value None is not the same as string None

def jointwo(a,b):
    joined = a + b
    return joined

x = jointwo(2,5)
print(x)

def fred():
    print("ZAP")

def jane():
    print('ABC')

jane()
fred()
jane()
 #EXERCISE 4.14
while True:
  try:
    hours = input('Enter Hours\n')
    hours = int(hours)

    rate = input('Enter Rate\n')
    rate = float(rate)

    def computepay():
        pay = hours * rate
        return pay

    if hours > 40:
       print (computepay() * 0.5)

    if hours <= 40:
       print(computepay())
  except:
    print('Error, Please enter numeric input')


#CHAMPTER 5 ITERATION

#While statements

i = 1
while i<= 12:
    print(i * '*')
    i = i + 1


J = 22
while J > 0:
    print(J)
    J = J - 1
print('Boom Shakalaka')

#Finishing iterations with continue

numbers = [ 1, 2, 3, 4, 5,]
for thing in numbers:
    print(thing)

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

numbers = range(5,10, 2)
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



#Definite loops using for
friends = ['Ace', 'Bsal', 'Bib', 'Kal']
for friend in friends:
    print('Wassup', friend)

#Counting and Summing loops
total = 0
for intervar in [3, 41, 12, 9, 74, 15]:
    total = total + intervar
print('Total:',total)

#Mximum and Minimum loops
largest = None
print('Before:' , largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    print('loop:' , itervar, largest)
print('Largest:' , largest)


smallest = None
print('Before:' , smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar > smallest :
        largest = itervar
    print('loop:' , itervar, smallest)
print('Smallest:' , smallest)

#Exercise 5.9 uncompleted
total = 0
while True:

    line = input("Enter a number")
    line = line(int)

    if line < '10':
        print(line)
        continue
    if line == 'done':
        break

    for intervar in [line]:
        total = total + intervar
    print('Total:', total)

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

for char in fruit:
    print(char)

#String slices

title = "Python Automation Guru"
        #0123456789
print(title.upper())
print(title.lower())
print(title.find('i'))
print(title.replace('Guru', 'Enthusiast'))
print(title )
print('Guru' in title)


s = 'monty python'
print(s [0:5])
print(s[6:12])

print(fruit[:3])
print(fruit[3:])

#Strings are immutable
fruit = 'banana'
greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)

#The in operator/Looping and Counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

#String Comparison
word = 'banana'
if word == 'banana':
  print('All right, bananas.')

if word < 'banana':
    print('Your word,' + word + ' ,  comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

#Strings methods/parsing strings
word = 'banana'
new_word = word.upper()
print(new_word)

word = 'banana'
index = word.find('na', 4)
print(index)

line = '  Here we go  '
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

#Format operator
camels = 42
'%d' % camels
print('i have spoted %d camels.' %camels)


#exercise 6.14
data = 'X-DSPAM-Confidence:0.8475'
atpos = data.find('0')
print(atpos)
print(data[19:25])
float(0.8475)

#Restart and understand everything

while True:
  try:
        s = input("What?")

        if s == ("I Love You Python") :
            print('I Love You Too Capt Jay')
            break

        else:
            print("I don't know what you're saying")

  except:
       print("You're not serious")

#Lists

names =["Kal", "Sal", "Bal", "Dal"]
names[0]="kall"
print(names[0:0])
print(names)

numbers = [ 1, 2, 3, 4, 5,]
numbers.append(6)
numbers.insert(0, -1)
numbers.remove(3)

print(7 in numbers)
print(len(numbers))

numbers = (1,2,3,3)
print(numbers.count(3))
