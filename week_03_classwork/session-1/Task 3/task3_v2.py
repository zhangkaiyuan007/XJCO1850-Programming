# Sample items with their prices
items = {
    "apple": 0.5,
    "banana": 0.3,
    "orange": 0.8,
    "grapes": 2.0,
    "watermelon": 3.0
}

# Get user input
item_selected = input("Enter the item you want to purchase (apple, banana, orange, grapes, watermelon): ").strip().lower()

# Quantity input with basic validation
try:
    quantity = int(input("Enter the quantity: "))
    if quantity <= 0:
        raise ValueError("Quantity must be positive.")
except ValueError as e:
    print("Invalid quantity:", e)
    exit()

# Initialize total cost
total_cost = 0

# Calculate total cost using if/elif
if item_selected == "apple":
    total_cost = items["apple"] * quantity
elif item_selected == "banana":
    total_cost = items["banana"] * quantity
elif item_selected == "orange":
    total_cost = items["orange"] * quantity
elif item_selected == "grapes":
    total_cost = items["grapes"] * quantity
elif item_selected == "watermelon":
    total_cost = items["watermelon"] * quantity
else:
    print("Item not available.")

# Print total cost if valid
if total_cost > 0:
    print(f"The total cost for {quantity} {item_selected}(s) is: £{total_cost:.2f}")
