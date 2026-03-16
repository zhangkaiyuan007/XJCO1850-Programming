import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print("Circle:")
        for i in range((self.radius * 2) + 1):
            for j in range((self.radius * 2) + 1):
                # Calculate distance from center to determine if '*' should be printed
                distance = ((i - self.radius) ** 2 + (j - self.radius) ** 2) ** 0.5
                if distance < self.radius + 0.5:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print("\n")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print("Rectangle:")
        for i in range(self.height):
            for j in range(self.width):
                # Draw '*' at the borders, otherwise draw space
                if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print("\n")


class Square:
    def __init__(self, side):
        self.side = side

    def draw(self):
        print("Square:")
        for i in range(self.side):
            for j in range(self.side):
                # Draw '*' at the borders, otherwise draw space
                if i == 0 or i == self.side - 1 or j == 0 or j == self.side - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print("\n")


class Triangle:
    def __init__(self, height):
        self.height = height

    def draw(self):
        print("Triangle:")
        for i in range(1, self.height + 1):
            # Print spaces for centering the triangle
            print(" " * (self.height - i), end="")
            # Print '*' to form the triangle pattern
            print("* " * i)
        print("\n")
