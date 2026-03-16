
"""
Exercise 2.1: Create a Team Class and Add Pokémon (Stub)
- Create a Team class.
- Implement the add_pokemon method to add a Pokémon to the team.
- Ensure no duplicates and enforce a maximum team size of 6 Pokémon.
"""

import httpx

class Team:
    def __init__(self):
        """Initialize an empty team."""
        # TODO: Initialize an empty list to store team members
        self.members = []
    
    def add_pokemon(self, name):
        """Add a Pokémon to the team."""
        # TODO: Check if the team already has 6 Pokémon
            # TODO: If yes, print a message indicating the team is full
        if len(self.members) >= 6:
            print("Cannot add more Pokémon. The team is already full (6 Pokémon max)!")
            return
        
        # TODO: Check if the Pokémon is already in the team
            # TODO: If yes, print a message indicating duplication
        if name.lower() in [pokemon['name'] for pokemon in self.members]:
            print(f"{name.capitalize()} is already in your team!")
            return
        
        # TODO: Fetch Pokémon data from the PokéAPI
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        response = httpx.get(url)
        
        if response.status_code == 200:
            data = response.json()
            # TODO: Extract necessary details (name, types, image URL)
            pokemon_info = {
                'name': data['name'].capitalize(),
                'types': [t['type']['name'] for t in data['types']],
                'image_url': data['sprites']['front_default']
            }
            # TODO: Add the Pokémon to the team
            self.members.append(pokemon_info)
            print(f"{pokemon_info['name']} has been added to your team.")
        else:
            # TODO: Print an error message if the Pokémon is not found
            print(f"Error: Pokémon '{name}' not found!")

# Example usage
# team = Team()
# team.add_pokemon("squirtle")
# team.add_pokemon("charmander")
