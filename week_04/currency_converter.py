"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name:
"""


def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }

    if amount < 0:
        converted_amount = 0.0
    else:
        rate = conversion_rate[from_currency][to_currency]
        converted_amount = round(amount * rate, 2)

    return converted_amount

# Submit only this file currency_converter.py with the completed function.
# Do not add additional code for calling the function,
# or code to get user input.
