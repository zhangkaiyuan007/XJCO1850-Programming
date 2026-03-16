class Customer:
    def __init__(self, name, id):
        self.name = name
        self.customer_id = id

    def __str__(self):
        return f"Customer: {self.name} (ID: {self.customer_id})"

# define the __repr__ method
