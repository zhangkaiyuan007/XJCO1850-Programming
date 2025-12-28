# Task: Reverse the text on each line of a file and save it to a new file.

# Instructions:
# - get the file name from the user
# - Open the original file and read each line.
# - Reverse the text of each line word by word -> 'hello my name is george' -> 'george is name my hello'
# - Write the reversed lines into a new file - the output file name should be the input filename + _reverse.txt
# for example: 'story.txt' -> 'story.txt_reverse.txt'
filename = input("Please input the filename to reverse: ")
output_filename = filename + "_reverse.txt"

try:
    with open(filename, 'r', encoding='utf-8') as f_in, \
         open(output_filename, 'w', encoding='utf-8') as f_out:
        
        for line in f_in:
            words = line.strip().split()
            
            reversed_words = words[::-1]
            
            new_line = " ".join(reversed_words) + "\n"
            
            f_out.write(new_line)
            
    print(f"Reversed content has been saved to: {output_filename}")
except FileNotFoundError:
    print("Error: File not found.")