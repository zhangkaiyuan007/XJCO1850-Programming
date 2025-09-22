
animals = [ 'dog','cat','hamster','goldfish' ]

# not_fish = [ item for item in animals if item != 'goldfish']
not_fish = []
for item in animals:
  if item != 'goldfish':
    not_fish.append(item)

print(not_fish)

# write the equivalent for loop to create the not_fish list from animals
# print your result to verify it is the same