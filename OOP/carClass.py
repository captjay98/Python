#!/usr/bin/python3


class BMW:
     
    def __init__(self="", name="", model="", year=0, appeal=""):
        self.name = name
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
        
        
e39 = BMW("5 Series", "e39",  1998, "Timeless Design")
    
e46 = BMW("3 Series", "e46", 2006, "The Subline Inline 6")
    
e9x = BMW("3 Series", "E90, E92, E93", 2007, "The Fantastic N53")

    
    
