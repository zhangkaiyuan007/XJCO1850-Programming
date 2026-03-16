# Uses /proc on Linux to get info on memory usage
# The file /proc/meminfo stores local information.
# You can view this using 'more /proc/meminfo'
#
# usage: python meminfo.py
#
# on linux you can look in the '/proc/meminfo' file for details about system memory
# print some key information from the file
# eg. total, free, available memory

file_name = '/proc/meminfo' 
