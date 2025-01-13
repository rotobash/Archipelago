from typing import Optional
from BaseClasses import Location, Region

class PokemonXDLocation(Location):
    game: str = "Pokemon XD"
    area_name: str = ""
    room_id: int = 0

    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        name = data["Name"]
        self.area_name = data["AreaName"]
        self.room_id = data["RoomId"]
        super().__init__(player, name, address + data["Index"], parent)


class PokemonXDPokemonLocation(PokemonXDLocation):
    pokemon_index = 0
    shadow_index = 0

    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        if "PokemonIndex" in data:
            self.pokemon_index = data["PokemonIndex"]
        self.shadow_index = data["ShadowIndex"]
        super().__init__(player, address, parent, **data)

class PokemonXDTrainerBattleLocation(PokemonXDLocation):
    battle_index = 0

    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        self.battle_index = data["BattleIndex"]
        super().__init__(player, address, parent, **data)

class PokemonXDItemLocation(PokemonXDLocation):
    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        super().__init__(player, address, parent, **data)


