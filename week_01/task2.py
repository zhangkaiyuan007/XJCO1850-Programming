"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""
name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
save_input = input("Enter your monthly savings amount: ")
while not save_input.isdigit():
    print("Invalid amount")
    save_input = input("Enter your monthly savings amount: ")

save = int(save_input)


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
total = save * 12
print(f"You will save £{total} every year.")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
total_include_interest = total + total * 0.008
print(f"With interest, you will save £{total_include_interest:.2f} per year.")
