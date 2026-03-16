# Checks the validity of a University of Leeds student username

import re
import sys

# Usage: python username.py <username>

# UoL usernames for students starting in the 24/25 session should be of the form
#  [ 4 lower case letters + 4 numbers ]
# If you know about regular expressions you can use the re module to create one 

username = sys.argv[1]

# The output should be a validation that the string input is of the correct form  
