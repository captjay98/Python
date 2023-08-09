#!/usr/bin/env python3

print("Entry Point")

""" Data Structures """

# List

testList = [1, 2, "a", "b"]

print(type(testList))

for i in testList:
    print(i)

# Dictionaries

testDict = {
    1: {
        "name": "Jamal",
        "age": 24,
    },
    2: {
        "name": "person",
        "age": "21",
    },
}

print(type(testDict))

for k, v in testDict.items():
    print(k, v)

for k in testDict.keys():
    print(k)

for v in testDict.values():
    print(v)


# sets

testSet = {1, 2, 3, 4, 5}
print(type(testSet))

# tuples

testTuple = (1, 2, 3)
print(type(testTuple))


"""bytes"""
print(bytes(16))
print(bytes("❤️)", "utf-8"))
