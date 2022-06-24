#!/usr/bin/python3


class Car:
     
    def __init__(self="", name="", brand="", model="", year=0, appeal=""):
        self.name = name
        self.brand = brand
        self.model = model
        self.year = year
        self.appeal = appeal
         
    def run(self):
        print("The car is a {}".format(self.name))
    
    def prestige(self):
        print(f"It is from the {self.brand} brand")
        
    def value(self):
        print("it is a {} model".format(self.model))
        
    def age(self):
        print("The car is {:d} years old".format(2022 - self.year))
        
    def reason(self):
        print("One reason You should get this car is because {}".format(self.appeal))
        
        
        

    
koja = Car("Koja", "BMW", "e46", 2006, "The Subline Inline 6")
    
Anaconda = Car("Anaconda", "Honda", "cp1", 2007, "VTEC, need to say more??")
    
e9x = Car("E9x", "BMW', 'E90, E92", 2007, "The Fantastic N53")

koja.run()
koja.prestige()
koja.value()
koja.age()

    
    
