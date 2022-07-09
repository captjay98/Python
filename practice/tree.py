#!/usr/bin/python3
tree = 9
ast = 1
space = tree - 1
stump = tree - 1
while tree != 0:
    for i in range(space):
        print(" ", end='')

    for i in range(ast):
        print("*", end='')

    print()
    space -= 1
    ast += 2
    tree -= 1

for i in range(stump):
    print(" ", end='')
print("*")
