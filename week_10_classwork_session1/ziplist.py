# Lists contents of a zip archive
# usage: python ziplist.py <zipfile>
# eg. python ziplist.py testdir/test.zip

import sys
from zipfile import ZipFile   # methods in this module can be used

archive_filename = sys.argv[1]

# use zipfile methods to list the contents of the zip file
# test your script on the test.zip file
