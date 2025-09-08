# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
print(f"Modified String 1: {user_string.lower()}") # convert all the characters to lower case
print(f"Modified String 2: {user_string.upper()}") # convert all the characters to capital
print(f"Modified String 3: {user_string.strip()}") # remove the whitespace
print(f"Modified String 4: {user_string.replace('a', '@')}") # replace all the "a" with "@"
print(f"Modified String 5: {user_string.capitalize()}") # turn first character capital
print(f"Modified String 6: {user_string[::-1]}") # reverse the whole string
print(f"Modified String 7: {user_string.title()}") # convert the first character in words to capital 
print(f"Modified String 8: {len(user_string)}") # return the length of the string
print(f"Modified String 9: {user_string.find('a')}") # find the earlist appear "a"
print(f"Modified String 10: {user_string.count('a')}") # count the number of "a" in the string
print(f"Modified String 11: {user_string.startswith('Hello')}") # return True if the string start with 'Hello'
print(f"Modified String 12: {user_string.endswith('!')}") # return True if the string end with '!'
print(f"Modified String 13: {user_string.isalnum()}") # return True when the string only contains digit and alpha
print(f"Modified String 14: {user_string.isalpha()}") # return True when the string only contains alpha
print(f"Modified String 15: {user_string.isdigit()}") # return True when the string only contains digit



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!