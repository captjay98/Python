#!/usr/bin/python3

"""Define a Square."""


class Square:
    """Represent a Square."""
    
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width
        
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
    
    
aSquare = Square()

height = input("Enter height :-")
width = input("Enter width:-")

aSquare.height = height
aSquare.width = width

print("Height: ", aSquare.height)
print("Width: ", aSquare.width)

print("The Area is", aSquare.getArea())