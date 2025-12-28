"""
Exercise 3.2: Simulate a Turn-Based Battle (Class-Based)

In this exercise, you will create a Pokemon class and use it to simulate battles.
This demonstrates object-oriented programming principles: encapsulation, methods, and clear responsibilities.
"""

import httpx

class Pokemon:
    def __init__(self, name):
        self.name = name.lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        response = httpx.get(url)
        
        if response.status_code != 200:
            raise ValueError(f"Could not find Pokemon: {name}")
            
        data = response.json()
        base_stats = {s['stat']['name']: s['base_stat'] for s in data['stats']}
        
        self.stats = {
            'attack': self._calculate_stat(base_stats['attack']),
            'defense': self._calculate_stat(base_stats['defense']),
            'speed': self._calculate_stat(base_stats['speed'])
        }
        self.max_hp = self._calculate_hp(base_stats['hp'])
        self.current_hp = self.max_hp

    def _calculate_stat(self, base_stat, level=50, iv=15, ev=85):
        return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

    def _calculate_hp(self, base_stat, level=50, iv=15, ev=85):
        return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

    def attack(self, defender):
        damage = int((((2 * 50 * 0.4 + 2) * self.stats['attack'] * 60) / (defender.stats['defense'] * 50)) + 2)
        defender.take_damage(damage)
        return damage

    def take_damage(self, amount):
        self.current_hp -= amount
        if self.current_hp < 0:
            self.current_hp = 0

    def is_fainted(self):
        return self.current_hp <= 0

    def __str__(self):
        return f"{self.name.capitalize()} (HP: {self.current_hp}/{self.max_hp})"


def simulate_battle(pokemon1_name, pokemon2_name):
    p1 = Pokemon(pokemon1_name)
    p2 = Pokemon(pokemon2_name)

    print(f"--- BATTLE START: {p1.name.capitalize()} vs {p2.name.capitalize()} ---")
    print(p1)
    print(p2)
    print("-" * 30)

    if p1.stats['speed'] >= p2.stats['speed']:
        attacker, defender = p1, p2
    else:
        attacker, defender = p2, p1

    round_num = 1
    while not p1.is_fainted() and not p2.is_fainted():
        print(f"Round {round_num}:")
        damage = attacker.attack(defender)
        print(f"{attacker.name.capitalize()} deals {damage} damage to {defender.name.capitalize()}!")
        print(defender)
        
        if defender.is_fainted():
            print(f"\n{defender.name.capitalize()} fainted!")
            break
            
        attacker, defender = defender, attacker
        round_num += 1
        print("-" * 30)

    winner = p1 if not p1.is_fainted() else p2
    print(f"\n--- BATTLE END ---")
    print(f"Winner: {winner.name.capitalize()} with {winner.current_hp} HP remaining!")


if __name__ == "__main__":
    simulate_battle("pikachu", "bulbasaur")

    # Uncomment to test other battles:
    # simulate_battle("charmander", "squirtle")
    # simulate_battle("eevee", "jigglypuff")
