
words = "Python textbook"
vowels = "aeiou"

# find all the vowels in the words string 
result = sorted({c for c in words.lower() if c in vowels})

print(result)

# Test the code for different 'words' strings

# Modify the result to only show which vowels occur, not every occurrence.
# Sort the list alphabetically.
# Hint: consider the properties of different data structures