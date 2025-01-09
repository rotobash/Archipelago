from BaseClasses import Region

class PokemonXDRegion(Region):
    game: str = "Pokemon XD"
    areaId: int = 0

    def __init__(self, player, multiworld, hint = None, **data):
        self.areaId = data["AreaId"]
        name = data["Name"]
        super().__init__(name, player, multiworld, hint)

        self.add_exits()
