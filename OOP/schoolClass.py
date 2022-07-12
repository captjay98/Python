#!/usr/bin/python3

class School():
    """Creates a School Member"""

    def __init__(self, name, age):
        """Initialises a School Member"""
        self.name = name
        self.age = age

    def tell(self):
        print("My name is {}, i am {} years old".format(self.name, self.age), end='')

    def __str__(self):
        return "{} {}".format(self.name, self.age)


class Student(School):
    """A Student class"""

    def __init__(self, name, age, Marks):
        super().__init__(name, age)
        self.marks = Marks

    def tell(self):
        return ("My grade is ", self.marks)


class Teacher(School):
    """Defines a teacher class"""
    def __init__(self, name, age, rating):
        School.__init__(self, name, age)
        self.rating = rating

    def tell(self):
        print("My current rating is ", self.rating)


jam = Student("Jamal", 50, 99)

Teacher = Teacher("Jay", 60, 77)

print(Teacher)
