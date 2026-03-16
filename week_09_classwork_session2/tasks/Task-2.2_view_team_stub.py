"""
Exercise 2.2: View the Current Team (Stub)
- Implement a method to view the current team.
- Display each Pokemon's name, types, and image URL.
"""

import httpx

class Team:
    def __init__(self):
        """Initialize an empty team."""
        self.members = []
    
    def add_pokemon(self, name):
        """Add a Pokemon to the team."""
        if len(self.members) >= 6:
            print("Cannot add more Pokemon. The team is already full (6 Pokemon max)!")
            return
        if name.lower() in [pokemon['name'].lower() for pokemon in self.members]:
            print(f"{name.capitalize()} is already in your team!")
            return
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        response = httpx.get(url)
        if response.status_code == 200:
            data = response.json()
            pokemon_info = {
                'name': data['name'].capitalize(),
                'types': [t['type']['name'] for t in data['types']],
                'image_url': data['sprites']['front_default']
            }
            self.members.append(pokemon_info)
            print(f"{pokemon_info['name']} has been added to your team.")
        else:
            print(f"Error: Pokemon '{name}' not found!")
    
    def view_team(self):
        """View the current team with details."""
        if not self.members:
            print("Your team is empty.")
            return
        print("Your Team:")
        for idx, pokemon in enumerate(self.members, 1):
            types = ", ".join(pokemon["types"])
            print(f"{idx}. {pokemon['name']} | Types: {types} | Image: {pokemon['image_url']}")
    
# Example usage
# team = Team()
# team.add_pokemon("squirtle")
# team.add_pokemon("charmander")
# team.view_team()
