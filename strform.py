#!/usr/bin/python3

print("This is a {} {} \n".format("Hello", "world test"))
print("This is a {0:<5} {1:^10} World, Test!\n".format(5, "Hello"))
print("{:*^15s}\n".format("Hello"))
print("i ate {0:.13f} and {1:.0f} of a {2}".format(75.56767, 80.679, "Pizza"))

food = "Pizza"
print("Bsal gon buy {}\n".format(food))

for i in range (10):
    print("{:<5d} {:^5d} {:>5d}".format(i, i*i, i*i*i))
