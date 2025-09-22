# Your task is to:
# - add support for squares (area = side length * side length)
# - add support for some other 2D polygon and test it (trapezoid, rhombus, etc)
# CHALLENGE - only if you finish all tasks - create a version of this code which asks users to enter their own shape,
#             and based on what they enter, ask for the needed dimensions to calculate area.


# Sample data for shapes
shapes = [
    ("circle", 5), 
    ("rectangle", 4, 6), 
    ("triangle", 3, 4),
    ("square", 7),
    ("trapezoid", 3, 5, 4),
]


for shape in shapes:
    # calculate the area correctly per shape
    match shape:
        case ("circle", radius):
            area = 3.14 * radius ** 2
            print(f"The area of the circle with radius {radius} is {area:.2f}")
        case ("rectangle", width, height):
            area = width * height
            print(f"The area of the rectangle with width {width} and height {height} is {area:.2f}")
        case ("triangle", base, height):
            area = 0.5 * base * height
            print(f"The area of the triangle with base {base} and height {height} is {area:.2f}")
        case ("square", side):
            area = side * side
            print(f"The area of the square with side {side} is {area:.2f}")
        case ("trapezoid", base1, base2, height):
            area = 0.5 * (base1 + base2) * height
            print(f"The area of the trapezoid with bases {base1}, {base2} and height {height} is {area:.2f}")
        case _:
            print("Unknown shape.")
