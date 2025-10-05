
L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
sequence = [0]
k = 1
index = 0
while index < L - 1:
  next = sequence[index] - k
  if next > 0 and next not in sequence:
    sequence.append(next)
  else:
    sequence.append(sequence[index] + k)
  index = index + 1
  k = k + 1

# You may wish to use further output for testing purposes while you develop your code

[ print(item) for item in sequence ]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence
