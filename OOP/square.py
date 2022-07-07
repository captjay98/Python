#!/usr/bin/python3

"""Define a Shape."""


from curses.textpad import rectangle
import turtle


class Shapes:
    """Represent a Square."""

    def __init__(self, sides=4, height=0, width=0):
        self.sides = sides
        self.__height = height
        self.__width = width
        self.interior = (self.sides - 2) * 180
        self.angle = self.interior/self.sides
        self.line = 5
        self.color = "blue"

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
        """Function That draws a shape using turtle"""
        for i in range(self.sides):
            turtle.color(self.color)
            turtle.pensize(self.line)
            turtle.color()
            turtle.forward(self.__height)
            turtle.right(180-self.angle)

    def getArea(self):
        return int(self.__width) * int(self.__height)

    def __str__(self):
        if self.name == "Reactangle":
            return ("Height of {} = {}, Width = {} and sides = {}"
                    .format(self.name, self.__height,
                            self.__width, self.sides))
        else:
            return ("Size of {} = {} and sides = {}"
                    .format(self.name, self.__height, self.sides))


class Square(Shapes):
    def __init__(self, sides=4, height=0):
        super().__init__(sides, height)
        self.sides = sides
        self.name = "Square"


class Rectangle(Shapes):
    def __init__(self, sides=4, height=0, width=0):
        super().__init__(sides, height, width)
        self.__height = height
        self.__width = width
        self.sides = sides
        self.name = "Reactangle"
        self.line = 8
        self.color = "pink"

    def draw(self):
        """Function That draws a shape using turtle"""
        turtle.begin_fill()
        turtle.pensize(self.line)
        turtle.color(self.color)
        turtle.forward(self.__width)
        turtle.right(90)
        turtle.forward(self.__height)
        turtle.right(90)
        turtle.forward(self.__width)
        turtle.right(90)
        turtle.forward(self.__height)
        turtle.right(90)
        turtle.end_fill()


class Polygon(Shapes):
    def __init__(self, sides=5, height=0):
        super().__init__(sides, height)
        self.sides = sides
        self.name = "Polygon"

    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()


aSquare = Square(4, 300)
print("\n")
aRect = Rectangle(4, 200, 400)
print("\n")
poly = Polygon(5, 200)

poly.draw()
turtle.done()
