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
