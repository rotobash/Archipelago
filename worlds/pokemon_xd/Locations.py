from typing import Optional
from BaseClasses import Location, Region

class PokemonXDLocation(Location):
    game: str = "Pokemon XD"
    area_id: int = 0
    room_id: int = 0

    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        name = data["Name"]
        self.area_id = data["AreaId"]
        self.room_id = data["RoomId"]
        super().__init__(player, name, address, parent)


class PokemonXDShadowPokemonLocation(PokemonXDLocation):
    shadow_index = 0

    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        self.shadow_index = data["ShadowIndex"]
        super().__init__(player, address, parent, **data)

class PokemonXDPokespotPokemonLocation(PokemonXDLocation):
    pokespot = ""
    pokemon_index = 0

    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        self.pokespot = data["Pokespot"]
        self.pokemon_index = data["PokemonIndex"]
        super().__init__(player, address, parent, **data)

class PokemonXDTrainerBattleLocation(PokemonXDLocation):
    battle_index = 0

    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        self.battle_index = data["BattleIndex"]
        super().__init__(player, address, parent, **data)

class PokemonXDItemLocation(PokemonXDLocation):
    item_index = 0

    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        self.item_index  = data["ItemIndex"]
        super().__init__(player, address, parent, **data)


