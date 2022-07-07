#!/usr/bin/python3

"""Define a Shape."""


import turtle


class Shapes:
    """Represent a Square."""

    def __init__(self, sides=4, height=0, width=0):
        self.sides = sides
        self.__height = height
        self.__width = width
        self.interior = (self.sides - 2) * 180
        self.angle = self.interior/self.sides

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

    def draw(self):
        """Function That drawa a shape using turtle"""
        for i in range(self.sides):
            turtle.forward(self.__width)
            turtle.right(180-self.angle)
        turtle.done()

    def getArea(self):
        return int(self.__width) * int(self.__height)

    def __str__(self):
        return ("Height of {} = {}, Width = {} and sides = {}"
                .format(self.name, self.__height, self.__width, self.sides))


class Square(Shapes):
    def __init__(self, sides=4, height=0, width=0):
        super().__init__(sides, height, width)
        self.sides = sides
        self.__height = height
        self.__width = width
        self.name = "Square"


class Rectangle(Shapes):
    def __init__(self, sides=4, height=0, width=0):
        super().__init__(sides, height, width)
        self.sides = sides
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


class Polygon(Shapes):
    def __init__(self, sides=5, height=0, width=0):
        super().__init__(sides, height, width)
        self.sides = sides
        self.__height = height
        self.__width = width
        self.name = "Polygon"


aSquare = Square(4, 300, 300)
print("\n")
aRect = Rectangle(4, 200, 400)
print("\n")
poly = Polygon(5, 200, 200)
