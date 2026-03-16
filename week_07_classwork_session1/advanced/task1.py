# Define a Character class with the following properties:
# This Character class has four fields: name, health, attack_power, and level. When an instance of Character is
# created, the values for these fields are passed into the __init__ method. 
# - attack_power is between 10 and 100 inclusive,
# - health is between 0 and 100 inclusive,
# - level is between 1 and 9999 inclusive.

# This class has the following methods:

# (1) level_up: Increases the level by 1, up to a maximum of 9999. If maximum level is reached, it remains at 9999.
# No additional arguments are required.

# (2) level_down: Decrease the level by 1, down to 1. If minimum level is reached, it remains at 1. No additional
# arguments are required.

# (3) battle: Facilitates a battle between two Character instances. This method takes a single argument, another
# Character instance. The battle follows these rules:

# - If both characters have the same level:
#      - If both have the same attack power, reduce current character's health by 1. 
#        Health cannot drop below 0.
#      - If current character has higher attack power, increase the attack power by 5, capped at 100.
#      - If current character has lower attack power, decrease the attack power by 5

# - If the current character has a lower level:
#      - Reduce the health of the current character by the level difference, stopping at 0 if needed.
#      - Decrease the current character's attack power by 5, but not below 10.

# - If the current character has a higher level:
#      - Increase the level of the current character by 1, up to a maximum of 9999.
#      - Increase the current character's attack power by 5, capped at 100.

# Additional conditions:
# - If attack power reaches 100 during a battle, increase the level by 1 (up to 9999) and reset attack power to 10.
# - If health drops to 0 during a battle, reduce the level by 1 and reset health to 1. If health is at 
#   0 and level is already at 1, both remain unchanged. This health and level adjustment can happen once per battle.
# - If attack power drops to 10 and lower during a battle, reduce the level by 1, and the attack power remains at 10. This 
#   level adjustment can happen once per battle as well.








# Once completed, in a separate file, import this module and create two of your favourite characters and battle them out
# and print each character's final health, attack_power, and level at the end


# Feel free to adjust the battle rules to your liking
