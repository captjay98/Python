#!/usr/bin/python3

from pickletools import read_unicodestring4


class School():
    """Creates a School Member"""

    def __init__(self, fname, lname, age):
        """Initialises a School Member"""
        self.fname = fname
        self.lname = lname
        self.age = age


    def tell(self):
        print ("My name is {}, i am {} years old, i am a {}".format(self.fullname(), self.age, self.__class__.__name__), end='')

    def fullname(self):
        fn = self.fname + " " + self.lname
        return fn

    def __repr__(self):
        return 'School("{}", "{}", {})'.format(self.fname, self.lname, self.age)

    def __str__(self):
        return "{} {} {}".format(self.fname, self.lname, self.age)


class Student(School):
    """A Student class"""

    def __init__(self, fname, lname, age, Marks):
        super().__init__(fname, lname, age)
        self.marks = Marks


class Teacher(School):
    """Defines a teacher class"""
    def __init__(self,fname, lname, age, rating):
        School.__init__(self,fname, lname, age)
        self.rating = rating


class Inspector(School):
    def __init__(self, fname, lname, age, emps=None):
        super().__init__(fname, lname, age)


ade = School( "ade", "Tunde",  55)

bsal = Student( "moh", "Zombie", 99, 0)

print(bsal.tell())
