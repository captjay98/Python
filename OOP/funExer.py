#!/usr/bin/python3

from re import L
from tracemalloc import start
from unicodedata import name


class Ninja():

    _alias = "They are all Formidable Hidden Villages"
    __members = 0
    battles = 0

    def __init__(self, name="", rank="", powerLevel=0):
        self.name = name
        self.rank = rank
        self.__powerLevel = powerLevel
        
        Ninja.__members += 1

    @staticmethod
    def participants():
        return Ninja.__members

    @classmethod
    def about(cls):
        return(f"{cls._alias}")

    @classmethod
    def numofBattles(cls, val):
        cls.battles = val

    def knownFor(self):
        if self.name == "Naruto":
            print(f"{self.name} is known for being the "
                "Number one Crackhead Ninja")
        elif self.name == "Rock Lee":
            print(f"{self.name} is known for being the "
                "The Most Enthusiastic Ninja")
        else:
            print(f"{self.name} is known for what they're known for")

    @property
    def powerLevel(self):
        return self.__powerLevel

    @powerLevel.setter
    def powerLevel(self, value):
        self.__powerLevel = value

    def strength(self, speciality):
        if self.name == "Naruto":
            print(f"{self.name} is known for being the "
                "Number one Crackhead Ninja ")
            print(f"He loves using the {speciality}")

        elif self.name == "Rock Lee":
            print(f"{self.name} is known for being the "
                "The Most Enthusiastic Ninja")
            print(f"He loves using the {speciality}")
        else:
            print(f"{self.name} is known for what they're known for")


    def details(self):
        detail = ("His name is {} He is a {} and has a power level of {}"
                .format(self.name, self.rank, self.__powerLevel))
        return  detail

    def __str__(self):
        detail = ("His name is {} He is a {} and has a power level of {}"
                .format(self.name, self.rank, self.__powerLevel))
        return detail

    def __eq__(self, object):
        return self.name == object.name and self.rank == object.rank

    @staticmethod
    def start_powwer(powerLevel):
        if powerLevel < 400:
            return "You,re Out"
        else:
            return ("You're INN")


class LeafVillage(Ninja):

    _alias = "LeafVillage are the Strongest Hidden Village"

    def __init__(self, name, rank, powerLevel, upperhand):
        super().__init__(name, rank, powerLevel)
        self.upperhand = upperhand

    def inLeaf(self):
        return(f"{self.name} is known for causing trouble.")

    def allies(self):
        if self.name == "Naruto":
            self.team = ["Sasuke", "Sakura", "Sai"]
        x = ("{}'s teammates include {}, {} and {}"
            .format(self.name, self.team[0], self.team[1], self.team[2]))
        return x


class SandVillage(Ninja):

    _alias = "SandVillage are also a Strong Hidden Village"

    def __init__(self, name, rank, powerLevel, upperhand):
        super().__init__(name, rank, powerLevel)
        self.upperhand = upperhand

    def inSand(self):
        return (f"{self.name} was a calm and collected Person.")

    """def allies(self):
        if self.name == "Naruto":
            allie = ["Temari", "Kakunro"]
        x = (f"{self.name}'s allies include {allie[0]} and {allie[1]}")
        return x"""


naruto = LeafVillage("Naruto", "Hokage", 500, "Nine Tails")
narut = SandVillage("Naruto", "Hokage", 50, "Jinchuriki")
lee = Ninja("Rock Lee", "Chunin", 350)
kiba = Ninja("Kiba", "Chunin", 250) 

gaara = SandVillage("Gaara", "Hokage", 500, "Sand Beast")
temari = SandVillage("Temari", "Chunin", 500, "Wind Style")

Ninja.numofBattles(50)
print(Ninja.battles)

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


















"""
print("{} is the main character," 
        "He is currently the {}"
        "and has a power level of {}"
        .format(naruto.name, naruto.rank, naruto.powerLevel))
"""