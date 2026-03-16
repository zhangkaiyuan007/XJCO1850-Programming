import sys

# Take in a csv (any csv) and do some basic cleaning:
#
# - check each row has the right number of columns
# - put the header row into title case
# - change all other text to lowercase for consistency
#
# Flag any bad rows (wrong no. columns) as an error message.

file_name = sys.argv[1]

with open(file_name) as f:
    data = f.readlines()

header = data[0]

header = header.strip().split(",")
count = len(header)
header = [ x.title() for x in header ]

cleaned = []
cleaned.append(header)

# process the csv data line by line
# check for the correct number of columns
# flag incorrect rows
# write out a cleaned csv file

