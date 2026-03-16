import sys

# Count occurrences of a word in a file
# usage: python file_word_count.py <file> <word>
# example: python file_word_count.py testdir/dust_of_snow.txt snow

file_name = sys.argv[1]
word_to_find = sys.argv[2]

# Open the file and read its content

# Count how many times the word appears 
word_count = 0

# Handle singular or plural case
if word_count == 1:
    print(f"The word '{word_to_find}' appears {word_count} time in {file_name}.")
else:
    print(f"The word '{word_to_find}' appears {word_count} times in {file_name}.")
