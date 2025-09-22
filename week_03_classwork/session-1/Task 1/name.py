name = input("Please enter your name: ").strip()
if name:
 print(f"Welcome, {name.title()}")
else:
 print("You didn’t enter a name!")

# strip() can delete the whitespace
# title() can capital the first letter of every word