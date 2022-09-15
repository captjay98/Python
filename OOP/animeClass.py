#!/usr/bin/python3


from re import L
from tracemalloc import start
from unicodedata import name
from ninjaClass import Ninja


class LeafVillage(Ninja):

    _alias = "LeafVillage are the Strongest Hidden Village"

    def __init__(self, name, rank, powerLevel, upperhand):
        super().__init__(name, rank, powerLevel)
        self.upperhand = upperhand

    def inLeaf(self):
        return(f"{self.name} is known for causing trouble.")




class SandVillage(Ninja):

    _alias = "SandVillage are also a Strong Hidden Village"

    def __init__(self, name, rank, powerLevel, upperhand):
        super().__init__(name, rank, powerLevel)
        self.upperhand = upperhand

    def inSand(self):
        return (f"{self.name} was a calm and collected Person.")

    def allies(self):
        if self.name == "gaara":
            self.team = ["Temari", "Kakuro"]
        x = ("{}'s teammates include {} and {}"
            .format(self.name, self.team[0], self.team[1]))
        return x

naruto = LeafVillage("Naruto", "Hokage", 500, "Nine Tails")
narut = SandVillage("Naruto", "Hokage", 50, "Jinchuriki")
lee = Ninja("Rock Lee", "Chunin", 350)
kiba = Ninja("Kiba", "Chunin", 250) 

gaara = SandVillage("Gaara", "Hokage", 500, "Sand Beast")
temari = SandVillage("Temari", "Chunin", 500, "Wind Style")

Ninja.numofBattles(50)
print(Ninja.battles)

print(Ninja.participants())

print(gaara.allies())
"""
#print(narut)
print(naruto.inLeaf())
#print(naruto.allies())
print(gaara.inSand())
#print(gaara.allies())


#(kiba.start_powwer(300))
#(naruto.start_powwer(500))
#(Ninja.start_powwer(600))

#naruto.knownFor()

#lee.knownFor()

#kiba.knownFor()

#naruto.strength("Shadow Clown Jutsu")

#y = lee.details()
#print(y)
naruto.powerLevel = 900
#lee.strength("Leaf Hurricane")
print(naruto)
print(gaara)

gaara.powerLevel = 800
print(gaara)

#  print(naruto == narut)

print(LeafVillage.about())
print(SandVillage.about())

"""

print(Ninja.participants())


















"""
print("{} is the main character," 
        "He is currently the {}"
        "and has a power level of {}"
        .format(naruto.name, naruto.rank, naruto.powerLevel))
"""