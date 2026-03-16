# Pokemon Data Analysis - Starter Code
# Complete the functions below to create a working Pokemon analysis program

# Global variable to store pokemon data
pokemon_data = []

def load_pokemon_data():
    """Load and process Pokemon data from CSV file
    
    CSV columns: #,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
    """
    global pokemon_data
    filename = "pokemon.csv"
    
    try:
        with open(filename, "r") as f:
            data = f.readlines()
    except FileNotFoundError:
        print("Error: pokemon.csv not found!")
        return False
    
    print("Processing Pokemon data...")
    
    # TODO: Skip header row and process each line
    for line in data[1:]:  # Skip header
        line = line.strip()
        if line:
            row = line.split(",")
            if len(row) >= 13:  # Make sure we have all columns
                try:
                    # TODO: Create pokemon dictionary with converted data types
                    pokemon = {
                        "number": int(row[0]),
                        "name": row[1],
                        "type1": row[2],
                        "type2": row[3] if row[3].strip() else None,
                        "total": int(row[4]),
                        "hp": int(row[5]),
                        "attack": int(row[6]),
                        "defense": int(row[7]),
                        "sp_attack": int(row[8]),
                        "sp_defense": int(row[9]),
                        "speed": int(row[10]),
                        "generation": int(row[11]),
                        "legendary": row[12].strip() == "True"
                    }
                    pokemon_data.append(pokemon)
                except (ValueError, IndexError):
                    # Skip invalid rows
                    continue
    
    print(f"Loaded {len(pokemon_data)} Pokemon!")
    return True

def search_pokemon_by_name():
    """Search for a specific Pokemon by name"""
    name = input("Enter Pokemon name: ").strip().lower()
    
    # TODO: Search through all Pokemon
    for pokemon in pokemon_data:
        # TODO: Compare names (case-insensitive)
        if pokemon["name"].lower() == name:
            display_pokemon(pokemon)
            return
    
    print(f"Pokemon '{name}' not found!")

def display_pokemon(pokemon):
    """Display detailed information about a Pokemon"""
    print(f"\n--- {pokemon['name']} ---")
    print(f"Pokedex #: {pokemon['number']}")
    
    # TODO: Handle dual types
    # Hint: Check if pokemon['type2'] is None
    type_str = pokemon['type1']
    # TODO: Add second type if it exists
    if pokemon["type2"]:
        type_str = f"{type_str} / {pokemon['type2']}"
    print(f"Type: {type_str}")
    
    print(f"Generation: {pokemon['generation']}")
    print(f"Legendary: {'Yes' if pokemon['legendary'] else 'No'}")
    
    print(f"\nBase Stats:")
    # TODO: Display all stats nicely
    print(f"  HP:        {pokemon['hp']}")
    # TODO: Add remaining stats (attack, defense, sp_attack, sp_defense, speed, total)
    print(f"  Attack:    {pokemon['attack']}")
    print(f"  Defense:   {pokemon['defense']}")
    print(f"  Sp. Atk:   {pokemon['sp_attack']}")
    print(f"  Sp. Def:   {pokemon['sp_defense']}")
    print(f"  Speed:     {pokemon['speed']}")
    print(f"  Total:     {pokemon['total']}")

def pokemon_by_type():
    """Find all Pokemon of a specific type"""
    ptype = input("Enter Pokemon type: ").strip().title()
    matches = []
    
    # TODO: Search for Pokemon with matching type
    for pokemon in pokemon_data:
        # TODO: Check both type1 and type2 fields
        # Hint: pokemon['type1'] == ptype or pokemon['type2'] == ptype
        if pokemon["type1"] == ptype or pokemon["type2"] == ptype:
            matches.append(pokemon)
    
    if matches:
        print(f"\nFound {len(matches)} {ptype}-type Pokemon:")
        
        # TODO: Sort matches by name using bubble sort (no lambda!)
        # Hint: Compare pokemon["name"] values
        for i in range(len(matches)):
            for j in range(len(matches) - 1 - i):
                # TODO: Compare and swap if needed
                if matches[j]["name"].lower() > matches[j + 1]["name"].lower():
                    matches[j], matches[j + 1] = matches[j + 1], matches[j]
        
        # TODO: Display results (limit to first 15)
        for i, pokemon in enumerate(matches[:15]):
            # TODO: Display pokemon info
            print(f"  {pokemon['name']} - Total: {pokemon['total']}")
        
        if len(matches) > 15:
            print(f"  ... and {len(matches) - 15} more")
    else:
        print(f"No {ptype}-type Pokemon found!")

def strongest_pokemon():
    """Find the strongest Pokemon in different categories"""
    if not pokemon_data:
        print("No Pokemon data loaded!")
        return
    
    print("\n--- Strongest Pokemon by Category ---")
    
    # TODO: Categories to check
    stats = {
        "Total": "total",
        "HP": "hp", 
        "Attack": "attack",
        "Defense": "defense",
        "Speed": "speed"
    }
    
    for stat_name, stat_key in stats.items():
        # TODO: Find maximum value for this stat
        max_value = 0
        strongest = []
        
        for pokemon in pokemon_data:
            # TODO: Check if this pokemon has higher stat
            # TODO: If higher, start new list; if equal, add to list
            value = pokemon[stat_key]
            if value > max_value:
                max_value = value
                strongest = [pokemon]
            elif value == max_value:
                strongest.append(pokemon)
        
        # TODO: Display results
        print(f"\n{stat_name}: {max_value}")
        # TODO: Print names of strongest Pokemon
        names = ", ".join(p["name"] for p in strongest)
        print(f"  {names}")

def type_analysis():
    """Analyse average stats by Pokemon type"""
    ptype = input("Enter Pokemon type to analyse: ").strip().title()
    
    # TODO: Get all Pokemon of this type
    type_pokemon = []
    for pokemon in pokemon_data:
        # TODO: Check if pokemon matches the type
        if pokemon["type1"] == ptype or pokemon["type2"] == ptype:
            type_pokemon.append(pokemon)
    
    if not type_pokemon:
        print(f"No {ptype}-type Pokemon found!")
        return
    
    # TODO: Calculate averages
    total_hp = 0
    total_attack = 0
    total_defense = 0
    total_speed = 0
    count = len(type_pokemon)
    
    for pokemon in type_pokemon:
        # TODO: Add up all the stats
        total_hp += pokemon["hp"]
        total_attack += pokemon["attack"]
        total_defense += pokemon["defense"]
        total_speed += pokemon["speed"]
    
    print(f"\n--- {ptype}-type Pokemon Analysis ---")
    print(f"Number of {ptype}-type Pokemon: {count}")
    print(f"Average Stats:")
    # TODO: Display averages (divide totals by count)
    print(f"  HP:      {total_hp / count:.1f}")
    print(f"  Attack:  {total_attack / count:.1f}")
    print(f"  Defense: {total_defense / count:.1f}")
    print(f"  Speed:   {total_speed / count:.1f}")

def simple_battle():
    """Simple Pokemon battle based on total stats"""
    print("\n--- Pokemon Battle Simulator ---")
    
    # TODO: Get first Pokemon name and find it
    name1 = input("Enter first Pokemon name: ").strip().lower()
    pokemon1 = None
    # TODO: Search for pokemon1
    for pokemon in pokemon_data:
        if pokemon["name"].lower() == name1:
            pokemon1 = pokemon
            break
    
    if not pokemon1:
        print(f"Pokemon '{name1}' not found!")
        return
    
    # TODO: Get second Pokemon name and find it
    name2 = input("Enter second Pokemon name: ").strip().lower()
    pokemon2 = None
    # TODO: Search for pokemon2
    for pokemon in pokemon_data:
        if pokemon["name"].lower() == name2:
            pokemon2 = pokemon
            break
    
    if not pokemon2:
        print(f"Pokemon '{name2}' not found!")
        return
    
    # TODO: Battle calculation (simple total stats comparison)
    print(f"\nBattle: {pokemon1['name']} vs {pokemon2['name']}")
    # TODO: Display total stats for both
    # TODO: Determine winner and display result
    print(f"{pokemon1['name']} total: {pokemon1['total']}")
    print(f"{pokemon2['name']} total: {pokemon2['total']}")
    if pokemon1["total"] > pokemon2["total"]:
        print(f"Winner: {pokemon1['name']}!")
    elif pokemon2["total"] > pokemon1["total"]:
        print(f"Winner: {pokemon2['name']}!")
    else:
        print("It's a tie!")

def main_menu():
    """Display menu and handle user choices"""
    while True:
        print("\n=== Pokemon Data Explorer ===")
        print("1. Search Pokemon by name")
        print("2. Find Pokemon by type")
        print("3. Strongest Pokemon")
        print("4. Type analysis")
        print("5. Pokemon battle")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            search_pokemon_by_name()
        elif choice == "2":
            pokemon_by_type()
        elif choice == "3":
            strongest_pokemon()
        elif choice == "4":
            type_analysis()
        elif choice == "5":
            simple_battle()
        elif choice == "6":
            print("Thanks for exploring Pokemon data!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")

# Main program
if __name__ == "__main__":
    print("Loading Pokemon data...")
    if load_pokemon_data():
        main_menu()
    else:
        print("Failed to load data. Please ensure pokemon.csv is available.")

# TODO List for completion:
# 1. Complete load_pokemon_data() - convert string data to appropriate types
# 2. Complete pokemon_by_type() - search and sort functionality  
# 3. Complete strongest_pokemon() - find maximum values across categories
# 4. Complete type_analysis() - calculate averages for Pokemon types
# 5. Complete simple_battle() - compare Pokemon stats and determine winner
# 6. Add dual-type handling in display_pokemon() function
