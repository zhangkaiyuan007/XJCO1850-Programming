# Task: Create an exact copy of a file by reading its content and writing it to a new file.


# Instructions:
# - get the file name from the user
# - Open the original file and read its content.
# - Create a new file, and write the same content into it - the output file should be the input file name + _copy.txt
# e.g. story.txt -> story.txt_copy.txt

# Tip: Consider which file modes will let you read and write text data.
filename = input("Please input the filename: ")

output_filename = filename + "_copy.txt"

try:
    with open(filename, 'r', encoding='utf-8') as original_file:
        content = original_file.read()

    with open(output_filename, 'w', encoding='utf-8') as new_file:
        new_file.write(content)

    print(f"File successfully copied to: {output_filename}")
except FileNotFoundError:
    print("Error: File not found. Please check the filename.")