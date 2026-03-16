"""
Task 1.3: Saving and Loading JSON Files

Goal: Learn to save JSON data to a file and load it back.
"""

import json

# Data to save
data = {
    "userId": 102,
    "name": "Bob Brown",
    "email": "bob.brown@example.co.uk",
    "isActive": True
}

# TODO: Save the data to a file named "user.json" using json.dump()
with open("user.json", "w") as f:
    json.dump(data, f, indent=2)

# TODO: Load the data back from "user.json" using json.load() and print it
with open("user.json", "r") as f:
    loaded = json.load(f)
print(loaded)
