import random

# reading & cleaning the data
with open("names.txt") as f:
    names = f.readlines()
names = [ name.strip() for name in names ]

'''
names is a list of 1000 names - each name is 2 words long (in format: firstname surname).

You have three tasks:

Task 1:

Ask the user to enter a number, and pick that many random names out of the list.


Task 2:

Create 10 new random names by picking 10 random firstnames and combining them with 10 random surnames.

Task 3:

Shuffle the list and create 250 teams of 4 random people.
Hint: use a list-of-lists to store the teams.

'''