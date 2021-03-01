class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        else:
            pokemon_details = pokemon.pokemon_details()
            self.pokemon.append(pokemon)
            return f"Caught {pokemon_details}"

    def release_pokemon(self, pokemon_name: str):
        for pokemon in self.pokemon:
            if pokemon.name == pokemon_name:
                self.pokemon.remove(pokemon)
                return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        pokemons_details = self.get_pokemons_details()
        return f"Pokemon Trainer {self.name}\n" \
               f"Pokemon count {len(self.pokemon)}\n" + '\n'.join(pokemons_details)

    def get_pokemons_details(self):
        return [f"- {pokemon_obj.pokemon_details()}" for pokemon_obj in self.pokemon]


# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
