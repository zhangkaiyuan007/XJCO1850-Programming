class Product:
    def __init__(self, name, price):
        self.name = name
        self.set_price(price)

    def set_price(self, price):
        if price < 0 or not isinstance(price, (int, float)):
            raise ValueError("Price cannot be below 0 or not a number")
        self.price = price

    def __str__(self):
        return f"{self.name} - £{self.price}"

# define the __repr__ method

# write code to test the set_price method with assert
