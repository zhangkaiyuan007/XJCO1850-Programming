import matplotlib.pyplot as plt

import sys

try:
    filename = sys.argv[1]
except:
    print("Error: Need a filename")
    exit(1)

# count letters in the file using a dictionary
letters = {}   

# Extract letters and their frequencies as 2 lists: lets and frequencies
lets = []
frequencies = []

# Plot the histogram
plt.bar(lets, frequencies, color='purple')

# Saving it into filename.png
plt.savefig(f"{filename.split(".")[0]}.png")  # you can view the png image in the folder
