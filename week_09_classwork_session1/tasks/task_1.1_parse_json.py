"""
Task 1.1: Parsing and Accessing JSON Data

Goal: Learn to parse JSON strings and access nested data.
"""

import json

# JSON string
json_string = """
{
    "userId": 101,
    "name": "Alice Smith",
    "email": "alice.smith@example.co.uk",
    "isActive": true,
    "roles": ["admin", "editor"],
    "address": {
        "street": "45 Briggate",
        "city": "Leeds",
        "postcode": "LS1 6HF"
    },
    "lastLogin": "2025-11-21T14:30:00Z"
}
"""

# TODO: Parse the JSON string into a Python dictionary using json.loads()

# TODO: Access values such as name, email, and city from the parsed dictionary
