"""
Exercise 1.3: Custom Output (Raw vs Summary) (Stub)
- Fetch Pokemon data from the PokeAPI.
- Display either the full raw JSON or a summarised version based on a parameter.
"""

import httpx
import json

def fetch_pokemon_custom(name, display_raw=False):
    """Fetch Pokemon details and display either raw JSON or a summary."""
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = httpx.get(url)
    if response.status_code == 200:
        data = response.json()
        if display_raw:
            print(json.dumps(data, indent=4))
        else:
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
# fetch_pokemon_custom("squirtle")  # Display summary by default
# fetch_pokemon_custom("squirtle", display_raw=True)  # Display raw JSON

"""
Hints:
- Use json.dumps(data, indent=4) for raw JSON output.
- Extract specific keys like 'types', 'stats', and 'sprites' for summaries.
- Use if display_raw to toggle between outputs.
"""
