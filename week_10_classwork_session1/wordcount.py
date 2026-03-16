# Counts 'words' in a file, even if it has been compressed with gzip
# Usage: python wordcount.py <textfile>
# eg. python wordcount.py testdir/frankenstein.txt.gz

import gzip  # to handle zipped files look for gzip.open() to access the file
import sys

filename = sys.argv[1]

word_count = 0

# count the words in the file
# test your script on lorem.txt or frankenstein.txt.gz

print(word_count)
