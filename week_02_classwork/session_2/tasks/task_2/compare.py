# Week 2, Session 2: Task 2
# Simple Number Comparer

# Prompt the user to enter the numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Use an if statement to compare the two numbers

if num1 > num2: 
    print("The first number is bigger.")
elif num1 < num2:  
    print("The second number is bigger.")
else:
    print("Both numbers are Equal.")
