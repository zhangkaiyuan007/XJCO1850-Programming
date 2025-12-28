import sys
import os

if len(sys.argv) < 2:
    sys.stderr.write("Usage: python file_line_count.py <filename.txt>\n")
    sys.exit(1)

file_name = sys.argv[1]

if not os.path.exists(file_name):
    sys.stderr.write(f"File not found: python file_line_count.py {file_name}\n")
    sys.exit(1)

try:
    number_of_lines = 0
    with open(file_name, 'r') as f:
        for line in f:
            if line.strip():
                number_of_lines += 1
    
    print(f"{file_name} has {number_of_lines} lines")
except Exception:
    sys.exit(1)