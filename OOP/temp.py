

heightofSq = int(input("Enter lenght of square :-"))
aSquare.height = heightofSq
aSquare.width = aSquare.height
print("Height: ", aSquare.height)
print("Width: ", aSquare.width)
print("The Area is", aSquare.getArea())
aSquare.draw()

heightOfRect = int(input("Enter height of rectangleR :- "))
widthOfRect = int(input("Enter width of Rectangle :- "))
aRect.height = heightOfRect
aRect.width = widthOfRect
print("Height of Rectangle = ", aRect.height)
print("Width of Rectangle - ", aRect.width)

aRect.draw()


def draw(self):
        """Function That drawa a shape using turtle"""
        for i in range(self.sides):
            turtle.forward(self.__width)
            turtle.right(self.__height)
        turtle.done()