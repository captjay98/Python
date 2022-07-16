#!/usr/bin/python3
class Ninja():
    
    _alias = "They are all Formidable Hidden Villages"
    __members = 0
    battles = 0

    def __init__(self, name="", rank="", powerLevel=0):
        self.name = name
        self.rank = rank
        self.__powerLevel = powerLevel
        
        Ninja.__members += 1

    """def __del__(self):
        Deletes the called instance
        Ninja.__members -= 1

        if Ninja.__members != 1:
            print(f"There are {Ninja.__members} Ninjas left")
        else:
            print(f"There is only {Ninja.__members} left, {self.name} is the winner")"""

    def die(self):
        print(f"{self.name} has been killed")
        Ninja.__members -= 1
        if Ninja.__members != 1:
            print(f"There are {Ninja.__members} Ninjas left")
        else:
            print(f"There is only {Ninja.__members} left")


    @staticmethod
    def members():
        return Ninja.__members

    def participants():
        if Ninja.__members == 1:
            return f"There is only {Ninja.__members} Participant left"
        return f"There are {Ninja.__members} Participants left"

    @classmethod
    def about(cls):
        return(f"{cls._alias}")

    @classmethod
    def numofBattles(cls, val):
        cls.battles = val

    @property
    def powerLevel(self):
        return self.__powerLevel

    @powerLevel.setter
    def powerLevel(self, value):
        self.__powerLevel = value

    def knownFor(self):
        if self.name == "Naruto":
            print(f"{self.name} is known for being the "
                "Number one Crackhead Ninja")
        elif self.name == "Rock Lee":
            print(f"{self.name} is known for being the "
                "The Most Enthusiastic Ninja")
        else:
            print(f"{self.name} is known for what they're known for")

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

    def __repr__(self):
        return 'Ninja("{}", "{}", {})'.format(self.name, self.rank, self.__powerLevel)
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

x = Ninja("Naruto", "Hokage", 9999)

print(repr(x))
