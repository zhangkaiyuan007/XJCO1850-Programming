# Identify and correct the errors in the following class definition.

class Rectangle:
    def __init__(self, wid, high):
        height = high
        width = wid

    def set_height(self, high):
        self.height = high

    def set_width(wid):
        self.width = wid


# Once corrected, we can now create an instance of Rectangle
# and print the details of the router
rectangle1 = Rectangle(5, 8)
print(rectangle1.height)
print(rectangle1.width)

# we can also call the method
rectangle1.set_height(10)
print(rectangle1.height)
