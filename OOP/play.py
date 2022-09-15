from itertools import count


class Robot:
    pass

x = Robot()
y = Robot()

x.name =  "Hey"
x.build = 56

y.name = "hi"
y.build = 78

Robot.brand = "Kuka"
x.brand = "Thales"

print(getattr(x, 'energy', 50))


"""
def f(x): 
    return 66

f.x = 66
print(f.x)

def f(x):
    f.counter = getattr(f, counter, 0) + 1
    return "Monty Python"

for i in range(10):
    f(i)
print(f.counter)"""