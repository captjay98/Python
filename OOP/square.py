#!/usr/bin/python3

"""Define a Shape."""

from re import A
import turtle

class Shapes:
    """Represent a Square."""
    
    def __init__(self, height="0", width="0"):
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

    def draw(self):
        """Function That drawa a shape using turtle"""
        for i in range(self.sides):
            turtle.forward(self.__width)
            turtle.right(self.__height)
        turtle.done()

aSquare = Shapes(50,180)
#aRect = Shapes()
print(aSquare)
print(aSquare.height)
print(aSquare.width)

aSquare.draw()