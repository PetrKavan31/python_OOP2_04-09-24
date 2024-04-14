# Create a base class Shape to draw flat shapes.
# Define the following methods:
# ■■ Show() — print info about a shape;
# ■■ Save() — save a shape to a file;
# ■■ Load() — read a shape from a file.
# Define the derived classes:
# ■■ Square — a square defined by the coordinates of the upper
# left corner and the side length;
# ■■ Rectangle — a rectangle with the specified coordinates of
# the upper left corner and dimensions;
# ■■ Circle — a circle with the specified coordinates of the center
# and radius;
# ■■ Ellipse — an ellipse with the specified coordinates of
# the top corner of a circumscribed rectangle with its sides
# parallel to the coordinate axes, and the dimensions of this
# rectangle.
# Create a list of shapes, save the shapes to a file, load into
# another list, and display information about each shape.

import pickle


class Shape:
    def __init__(self):
        pass

    def show_shape(self):
        pass

    def save(self, filename):
        with open(filename, "rb") as file:
            pickle.dump(self, file)

    @staticmethod
    # cls???
    def load(filename):
        with open(filename, "rb") as file:
            return pickle.load(file)


class Square(Shape):
    def __init__(self, x, y, side_length):
        super().__init__()
        self.x = x
        self.y = y
        self.side_length = side_length

    def show_shape(self):
        return f"Square: Upper left corner: x = {self.x}, y = {self.y}, side length = {self.side_length}"


class Rectangle(Shape):
    def __init__(self, x, y, side_a, side_b):
        super().__init__()
        self.x = x
        self.y = y
        self.side_a = side_a
        self.side_b = side_b

    def show_shape(self):
        return f"Rectangle: Upper left corner: x = {self.x}, y = {self.y}, side a = {self.side_a}, side b = {self.side_b}"


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius

    def show_shape(self):
        return f"Circle: Center at: x = {self.x}, y = {self.y}, radius: {self.radius}"


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show_shape(self):
        return f"Top corner: x = {self.x}, y = {self.y}, width: {self.width}, height: {self.height}"


