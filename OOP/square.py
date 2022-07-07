#!/usr/bin/python3

"""Define a Shape."""


from re import A
from reprlib import aRepr
import turtle
from webbrowser import get


class Shapes:
    """Represent a Square."""

    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width
        self.sides = 4

    @property
    def height(self):
        print("Retrieving height")
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def width(self):
        print("Retrieving Width")
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    def getArea(self):
        return int(self.__width) * int(self.__height)

    def __str__(self):
        return ("Height of {} = {}, Width = {} and sides = "
                .format(self.name, self.__height, self.__width))

    def __init__(self, height=0, width=0):
        super().__init__(height, width)
        self.__height = height
        self.__width = width
        self.name = "Square"

    def draw(self):
        """Function That drawa a shape using turtle"""
        for i in range(self.sides):
            turtle.forward(self.__width)
            turtle.right(self.__height)
        turtle.done()


class Rectangle(Shapes):
    def __init__(self, height=0, width=0):
        super().__init__(height, width)
        self.__height = height
        self.__width = width
        self.name = "Reactangle"

    def draw(self):
        """Function That drawa a shape using turtle"""
        turtle.forward(self.__width)
        turtle.right(90)
        turtle.forward(self.__height)
        turtle.right(90)
        turtle.forward(self.__width)
        turtle.right(90)
        turtle.forward(self.__height)
        turtle.right(90)
        turtle.done()


aSquare = Square()
heightofSq = int(input("Enter lenght of square :-"))
aSquare.height = heightofSq
aSquare.width = aSquare.height
print(aSquare)

print("\n")

aRect = Rectangle(80, 180)
print(aRect)
aRect.draw()
