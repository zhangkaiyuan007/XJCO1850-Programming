"""
Exercise 1.2: Summarise Pokemon Details (Stub)
- Fetch Pokemon data from the PokeAPI.
- Extract specific details: name, types, stats, and image URL.
- Display the extracted details in a readable format.
"""

import httpx

def summarise_pokemon(name):
    """Fetch and summarise Pokemon details."""
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = httpx.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemon_name = data["name"].capitalize()
        types = [t["type"]["name"] for t in data["types"]]
        stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
        image_url = data["sprites"]["front_default"]
        print(f"Name: {pokemon_name}")
        print(f"Types: {', '.join(types)}")
        print("Base Stats:")
        for stat, value in stats.items():
            print(f"  {stat.capitalize()}: {value}")
        print(f"Image URL: {image_url}")
    else:
        print(f"Error: Pokemon '{name}' not found!")

# Example usage
# summarise_pokemon("squirtle")

"""
Hints:
- Use data['types'] for the Pokemon's types.
- Use data['stats'] for the Pokemon's base stats.
- Use a loop to format and display lists or dictionaries.
"""
