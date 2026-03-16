import os
import sys

# Find any files in the current folder and any sub-folders that contain a given string
# Print the full path to any file that matches the string.
# usage: python find_file.py <string>
# eg. python find_file.py test2

my_string = sys.argv[1]
basedir = os.getcwd()

# To explore the 'basedir' folder and subfolders look up the os.walk() method
# ( Alternatively you could write your own recursive solution to explore the folders )

