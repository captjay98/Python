#!/usr/bin/python3


class Robot:
    
    population = 0
    
    def __init__(self, name):
        
        """Initialize the Data"""
        
        self.name = name
        print(f"Initializing {self.name}")
        
        
        #When Robot is created, robot adds to the population
        
        Robot.population+=1
        
    def die(self):
        """I am dying"""
        print(f"{self.name} is being destroyed")
        
        Robot.population -= 1
        
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
            
        else:
            print(f"There are still {Robot.population} robots working")
            
            
    def sayhi(self):
        """Greeting the robot"""
        
        
        print(f"Greetings, my masters call me {self.name}")
        
    @classmethod
    def how_many(cls):
        """Prints current population"""
        print(f"we have {cls.population} robots")
        
        
droid1 = Robot("Sesame")
droid1.sayhi()
Robot.how_many()

droid0 = Robot("Kal")
droid0.sayhi()
Robot.how_many()

print("\n Robots can do some work here\n")

print("\nRobots have finished their work, so lets destoy them\n")

droid1.die()
droid0.die()


Robot.how_many()
