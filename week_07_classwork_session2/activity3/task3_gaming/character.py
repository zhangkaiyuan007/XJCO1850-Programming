# define a parent class called Character with the following fields:
# (1) name - the name of the character
# (2) health - the character's health points
# (3) level - the current level of the character, default to 1
# (4) attack_power - the character base attack power







# this class has the following methods:
# (1) attack() - print a message that the character attacks with their attack power.
#     e.g., Naruro attacks with power 50. Note: you are not writing code for actual attacking
# (2) take_damage(amount) - reduces health by the specific damage amount and prints the updated health. 
#     If health reaches 0 or below, print a message that the character has been defeated
# (3) level_up() - increases the character's level by 1, boost the health by 20, attack_power by 5,
#     and prints a message indicating the character leveled up, e.g., Naruto leveled up to 22
# (4) __str__ - to return a summary of the character's name, level, health, and attack power,
#     e.g., Character 'Naruto' - Level: 1, Health: 100, Attack Power: 20






# write code to define subclasses for specific Character classes as follows:
# (1) Warrior class with the following fields and methods:
#     - armor - the armor points, reduces damage taken in take_damage
#     - power_strike() - prints a message indicating a special attack with increased attack power#
#       e.g., Naruto perfoms a Power Strike with 2x power!
#     - take_damage(amount) - override parent class's take_damage method to reduce damage by the armor amount
#       e.g., if original damage amount is 100 and armor is 10, now the damage amount is 100 - 10 = 90
#     - __str__ - override the __str__ to include the armor


# (2) Mage class with the following fields and methods:
#     - mana - a resource used to cast spells
#     - cast_spell() - reduces mana and prints a message indicating a spell has been cast with increased attack power.
#       e.g., Merlin casts a powerful spell with 1.5x power! When this method is called, reduce the mana by 20. If
#       the mana is insufficient, print a different message, e.g., Merlin does not have enough mana to cast the spell.
#     - attack() - override attack() to cast a basic spell instead of physical attack by printing a different message, 
#       e.g., Merlin casts a spell with power 40.
#     - __str__ - override the __str__ to include mana



# (3) Archer class with the following fields and methods
#     - arrows - the number of arrows available to shoot
#     - shoot_arrow() - reduces arrows and prints a message indicating a ranged attack,
#       e.g., Hawkeye performs a ranged attack with power 80. If insufficient arrow, prints a different message,
#       e.g., Hawkeye is out of arrows
#     - attack() - override attack() to use arrows when attacking by printing a different message,
#       e.g., Hawkeye shoots an arrow with power 78.
#     - __str__ - override the __str__ to include arrows


# feel free to update Character and subclasses with more fields and methods



