#!/usr/bin/python3
word = "This is a test file"

x = len(word)

print(x)

'{} {}'.format('one', 'two')

'{:>10}'.format('test')

'{:10}'.format('test')

'{:_<10}'.format('test')

'{:^10}'.format('test')

'{:.5}'.format('xylophone')

'{:10.5}'.format('xylophone')

'{:d}'.format(42)

'{:f}'.format(3.141592653589793)

'{:4d}'.format(42)

'{:06.2f}'.format(3.141592653589793)

'{:+d}'.format(42)

'{: d}'.format((- 23))

'{: d}'.format(42)

'{:=5d}'.format((- 23))

'{:=+5d}'.format(23)

'{first} {last}'.format(**data)

'{first} {last}'.format(first='Hodor', last='Hodor!')
#!/usr/bin/python3

print("This is a {} {} \n".format("Hello", "world test"))
print("This is a {0:<5} {1:^10} World, Test!\n".format(5, "Hello"))
print("{:*^15s}\n".format("Hello"))
print("i ate {0:.13f} and {1:.0f} of a {2}".format(75.56767, 80.679, "Pizza"))

food = "Pizza"
print("Bsal gon buy {}\n".format(food))

for i in range (10):
    print("{:<5d} {:^5d} {:>5d}".format(i, i*i, i*i*i))
