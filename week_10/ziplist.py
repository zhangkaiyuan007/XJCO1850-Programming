import sys
import os
import zipfile

if len(sys.argv) < 2:
    sys.stderr.write("Usage: python ziplist.py <file.zip>\n")
    sys.exit(1)

file_name = sys.argv[1]

if not os.path.exists(file_name):
    sys.stderr.write(f"File not found: python ziplist.py {file_name}\n")
    sys.exit(1)

if not zipfile.is_zipfile(file_name):
    sys.stderr.write(f"Bad zip file: python ziplist.py {file_name}\n")
    sys.exit(1)

try:
    with zipfile.ZipFile(file_name, 'r') as z:
        for name in z.namelist():
            print(name)
except Exception:
    sys.exit(1)