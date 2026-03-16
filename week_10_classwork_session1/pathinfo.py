# Using the pathlib module: 
# https://docs.python.org/3/library/pathlib.html

# usage: python pathinfo.py

from pathlib import Path

file_path = Path("testdir/subdir1/test2.txt")

print("Path:", file_path)

# test some pathlib features
# is_file(), is_dir()
# name, stem, suffix, parent

