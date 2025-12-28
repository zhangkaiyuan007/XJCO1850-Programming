'''
Create a program which simulates rolling a 6-sided die a number of times. The user should enter the number of times they want to the dice to be rolled, and the program will then print each one.
Example:
python dice.py
How many times should I roll the die?: 3
You have rolled a 3
You have rolled a 6
You have rolled a 1

This involves inputting a number, so you should ensure your code is robust and can handle unusual inputs such as negatives or non-numerical values.

Extension:
You could also create a class ‘Dice’ and allow users to generate a die with any (valid) number of sides.
'''
import random

def main():
    try:
        user_input = input("How many times should I roll the die?: ")
        num_rolls = int(user_input)
        
        if num_rolls <= 0:
            print("Please enter a positive number of rolls.")
        else:
            for _ in range(num_rolls):
                result = random.randint(1, 6)
                print(f"You have rolled a {result}")
                
    except ValueError:
        print("Invalid input. Please enter a whole numerical value.")

if __name__ == "__main__":
    main()
