#!/usr/bin/python3
import datetime

class EmPloyee:
    
    num_of_emps = 0
    raise_amount = 1.05
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@mail.com"
        
        EmPloyee.num_of_emps += 1
        
    def full_name(self):
        return "{} {}".format(self.first, self.last)
        
    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amount)
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 0:
            return False
        return True 

emp5 = EmPloyee("Jay", "Ibro", 50000)
emp6 = EmPloyee("Kal", "Abs", 90000)
emp7 = EmPloyee("Sal", "Moh", 70000)

emp5.raise_amount = 1.55
EmPloyee.set_raise_amount( 1.77)

print(emp5.first)
print(emp6.last)
print(emp7.raise_amount)

emp_str = "Jamal-Ibrahim-80000"
new_emp5 = EmPloyee.from_string(emp_str)

print(new_emp5.email)

my_date = datetime.date(2016, 7, 11)

print(EmPloyee.is_workday(my_date))



























"""
class person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sayhi(self):
        
        print("Hello, my name is " + self.name)
        print(f"I am {self.age} years old")

person("Jamal", 23).sayhi()  
p = person("Jamal", 23)
p.sayhi() """

