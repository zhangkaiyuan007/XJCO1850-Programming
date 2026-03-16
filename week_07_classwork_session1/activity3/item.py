# Define an InventoryItem class to represent an item in a warehouse.
# This class will allow for tracking stock, updating quantities, and 
# calculating the total value of the stock.

# This class has the following fields:
# (1) name: the name of the inventory item (e.g., Laptop)
# (2) sku: a unique stock keeping unit idenfier for the item (e.g., LPT001)
# (3) quantity: the current quantity of the item in stock
# (4) price_per_unit: the price per unit of the item

# This class has the following methods:
# (1) add_stock(amount): add the specific amount to the current stock quantity
# (2) remove_stock(amount): reduces the quantity of the item in stock by the specific amount.
#     If the amount to be removed is greater than current stock quantity, set the quantity to 0.
# (3) get_total_value(): calculates and returns the total value of the stock on hand based
#     based on the current quantity and price_per_unit. If quantity is 0, return a 0.
# (4) display_item(): prints the details of the item including the name, sku, quantity,
#     price_per_unit, and the total stock value (calculated using get_total_value())