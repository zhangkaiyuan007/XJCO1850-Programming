"""
Exercise 3.1: Fetch and Compare Pokémon Stats (Stub)
- Fetch data for two Pokémon from the PokéAPI.
- Calculate their stats at level 50.
- Compare their base stats (e.g., attack, defense, speed).
"""

import httpx

def calculate_stat(base_stat, level=50, iv=15, ev=85):
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

def calculate_hp(base_stat, level=50, iv=15, ev=85):
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

def compare_pokemon(pokemon1, pokemon2):
    names = [pokemon1.lower(), pokemon2.lower()]
    all_stats = []

    for name in names:
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = httpx.get(url)
        if response.status_code != 200:
            print(f"Could not find {name}")
            return
        
        data = response.json()
        base = {s['stat']['name']: s['base_stat'] for s in data['stats']}
        
        final_stats = {
            "hp": calculate_hp(base['hp']),
            "attack": calculate_stat(base['attack']),
            "defense": calculate_stat(base['defense']),
            "speed": calculate_stat(base['speed'])
        }
        all_stats.append(final_stats)

    p1_vals = all_stats[0]
    p2_vals = all_stats[1]
    categories = ["hp", "attack", "defense", "speed"]

    print(f"Comparing {pokemon1.capitalize()} and {pokemon2.capitalize()} at Level 50:")
    for cat in categories:
        val1 = p1_vals[cat]
        val2 = p2_vals[cat]
        
        if val1 > val2:
            winner = pokemon1.capitalize()
        elif val2 > val1:
            winner = pokemon2.capitalize()
        else:
            winner = "Tie"
            
        print(f"{cat.upper():<8}: {val1:>3} vs {val2:>3} | Higher: {winner}")

if __name__ == "__main__":
    compare_pokemon("pikachu", "bulbasaur")

"""
Hints:
- Use httpx.get(url) to fetch data for each Pokémon.
- Access base stats using data['stats'] and extract base_stat values.
- Use calculate_stat and calculate_hp to compute level 50 stats.
"""
