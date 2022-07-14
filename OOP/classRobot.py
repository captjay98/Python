#!/usr/bin/python3
from distutils.command.build import build
from os import stat


class Robot:
    """Represent a robot object"""

    __population = 0

    def __init__(self, name=None, buildYear=0, rating=0):
        """Initialize a New Robot"""

        if name is not None:
            self.name = name
            print(f"Initializing {self.name}")
        else:
            self.name = "NoName"
            print(f"Initializing {self.name}")
            
        self.__buildYear = buildYear
        self.__rating = rating

        #When Robot is created, robot adds to the __population
        Robot.__population+=1

    def __del__(self):
        """Kills a Robot"""
        print(f"{self.name} is being destroyed")
        #When Robot is killed, robot subs from the __population
        Robot.__population -= 1

        if Robot.__population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.__population} robots working")

    def buildYear(self):
        return self.__buildYear

    def buildYear(self, year):
        self.__buildYear = year

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        self.__rating = rating

    def die(self):
        """Kills a Robot"""
        print(f"{self.name} is being destroyed")
        #When Robot is killed, robot subs from the __population
        Robot.__population -= 1

        if Robot.__population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.__population} robots working")

    @staticmethod
    def Robot_population():
        return Robot.__population

    def sayhi(self):
        """Robot greets"""
        if self.name is not None:
            print(f"Greetings, my masters call me {self.name}")
        else:
            print("Greetings, my masters didn't give me a name")

        if self.__buildYear != 0:
            print(f"I was born in {self.__buildYear}")
        else:
            print("I don't know When i was born")

    def __repr__(self):
        return "Robot('" + self.name + "', " + str(self.__buildYear) + ")"

    def __str__(self):

        if self.__rating != 0:
            return ("My masters call me {}, I was Manufactured in the year {} and i have a rating of {}"
                .format(self.name, self.__buildYear, self.__rating))
        else:
            return ("My masters call me {}, I was Manufactured in the year {}"
                .format(self.name, self.__buildYear))

    @classmethod
    def how_many(self):
        """Prints current __population"""
        print(f"we have {self.__population} robot(s)")


droid1 = Robot("Sesame", 2002, 90)
print(droid1)
"""
x = str(droid1)
print(x)
print(type(x))

y = repr(droid1)
print(y)
print(type(y))
n = eval(y)
print(type(n))
"""
droid1.sayhi()
Robot.how_many()
print()

droid0 = Robot("Kal")
droid0.buildYear(2005)
print(droid0)
droid0.sayhi()
Robot.how_many()
print()

droid5 = Robot()
droid5.sayhi()
Robot.how_many()
print()

print(Robot.Robot_population())

del droid1
print()
del droid5
print()
del droid0
print()
Robot.how_many()

