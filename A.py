class Human:

    def __init__(self, name, age, occupation, height, weight, complexion):
        self.name = name
        self.occupation = occupation
        self.age = age
        self.height = height
        self.weight = weight
        self.complexion = complexion

    def likes(self):
        if self.name == "Jamal":
            print(self.name, "PlaYS Xbox games alot")
        elif self.name == "random":
            print(self.name, "does what humans do")

    def speaks(self):
        print(self.name, "Speaks English")

    def loves(self):
        if self.occupation == "Programmer":
            print(self.name, "Loves Python")
        elif self.occupation == "Graduate":
            print(self.name, "Just doing regular work")


me = Human("Jamal", 23, "Programmer", 180, 65, 'dark')
me.likes()
me.loves()
me.speaks()

print(f"Jamal is {me.age} years old")
print(f"He is {me.height}CM Tall")
print(f"And weighs {me.weight}KG")
