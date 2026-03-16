import sys

print(f"sys.argv is a {type(sys.argv)}")   # sys.argv is a list

n = len(sys.argv)
print(f"Total arguments passed:", n)

for item in sys.argv:   # iterate through the list
    print(f"Type: {type(item)} Value: {item}")   # all items are strings
