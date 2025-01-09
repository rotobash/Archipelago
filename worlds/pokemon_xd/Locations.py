from BaseClasses import Location

class PokemonXDLocation(Location):
    game: str = "Pokemon XD"

    def __init__(self, player, address = None, parent = None, **data):
        name = data["Name"]
        super().__init__(player, name, address, parent)


class PokemonXDPokemonLocation(PokemonXDLocation):
    pokemon_index = 0