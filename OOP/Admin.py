class User:
    def __init__(self, email):
        self.email = email
        
    def sign_in(self):
        print("Logged In")
        

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def attack(self):
        self.attack
        print("Attacking with the power of {}".format(self.power))
    
class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
        
    def attac(self):
        self.attac
        print("Attacking with the power of {}".format(self.arrows))
        
        
class WizardArcher(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name,  power)
        Archer.__init__(self, name,  arrows)
    
    
dumbld = Wizard("Dumbledore", 90)
arch = Archer("Robin", 90)

dumbldarch = WizardArcher("Merlin", 70, 50)

print(dumbld.name)
print(dumbld.power)
print(dumbld.attack())

print(arch.name)
print(arch.arrows)
print(arch.attac())

print(dumbldarch.name)
print(dumbldarch.power)
print(dumbldarch.arrows)
print(dumbldarch.attack())
print(dumbldarch.attac())