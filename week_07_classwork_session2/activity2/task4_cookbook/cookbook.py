# write code to import the recipe module



# define a Cookbook class with the following fields:
# (1) name - the name of the cookbook
# (2) author - the author of the cookbook
# (3) isbn - the isbn of the cookbook
# (4) recipes - a list of Recipe instances, representing each Recipe in the cookbook



# this class has the following methods:
# (1) __init__ - to initialise name, author, isbn, and recipes. the field
#     recipes is initialised to an empty list. When an instance of Cookbook is 
#     created, only the value for name, author, and isbn is required
# (2) add_recipe(self, recipe) - adds a Recipe instance to the list (i.e., recipes)
# (3) get_recipe(self, name) - finds a recipe by name and returns the full recipe
#     details using the display_recipe method from the recipe class. If a recipe
#     is not found, returns "not found"
# (4) __str__ - returns a summary of the cookbook with information on the 
#     name of the cookbook, author, isbn, and a list of the names of all recipes 
