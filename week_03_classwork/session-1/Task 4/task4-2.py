# Adapt this code to use a match instead of an if statement
# you could also:
# - make the inputs more robust
# - try and add a loop to make the program repeat (if you have done python before)


while True:
  # Display the menu
  print("Select an operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")

  # Get user choice
  choice = input("Enter your choice (1-5): ")
  if choice == "5":
    print("Exiting the program.")
    break
  # Get numbers to operate on
  try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
  except ValueError:
    print("Invalid input! Please enter numeric values.")
    continue

  # Process the choice using if statements
  match choice:
    case "1":
      result = num1 + num2
      print(f"The result of addition is: {result}")
    case "2":
      result = num1 - num2
      print(f"The result of subtraction is: {result}")
    case "3":
      result = num1 * num2
      print(f"The result of multiplication is: {result}")
    case "4":
      if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
      else:
        print("Error: Cannot divide by zero.")
    case _:
      print("Invalid choice. Please select a number between 1 and 5.")
