# Task: Open a file and calculate the total number of lines, words, and characters.

# Instructions:
# - get the file name from the user
# - Read the file contents.
# - Count how many lines, words, and characters are in the file.
# - Print out the totals for each.
filename = input("Please input the filename to analyze: ")

try:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    num_lines = len(lines)
    num_words = 0
    num_chars = 0

    for line in lines:
        num_chars += len(line)
        words = line.split()
        num_words += len(words)

    print(f"Total lines: {num_lines}")
    print(f"Total words: {num_words}")
    print(f"Total characters: {num_chars}")

except FileNotFoundError:
    print("Error: File not found.")