import sys

try:
    grade = int(input("Please input your grade(an integer in the range 0 to 100): "))
except ValueError:
    sys.exit("Error: Grade must be an integer between 0 and 100.")

if grade > 100 or grade < 0:
    sys.exit("Error: Grade must be an integer between 0 and 100.")

if grade >= 70 and grade <= 100:
    print(f"{grade} is a Distinction")
elif grade >= 40 and grade <= 69:
    print(f"{grade} is a Pass")
elif grade >= 0 and grade <= 39:
    print(f"{grade} is a Fail")



