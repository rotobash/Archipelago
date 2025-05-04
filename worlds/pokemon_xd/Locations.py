from typing import Optional
from BaseClasses import Location, Region

class PokemonXDLocation(Location):
    game: str = "Pokemon XD"
    category: str = ""
    area_name: str = ""
    room_id: int = 0
    index: int = 0

    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        name = data["Name"]
        self.index = data["Index"]
        self.category = data["Metadata"]["Category"]
        self.area_name = data["Metadata"]["AreaName"]
        self.room_id = data["Metadata"]["RoomId"]
        super().__init__(player, name, address + data["Index"], parent)

    def to_json(self):
        return {
            "Name": self.name,
            "Index": self.index,
            "AreaName": self.area_name,
            "RoomId": self.room_id,
            "Category": self.category,
        }


class PokemonXDPokemonLocation(PokemonXDLocation):
    pokemon_index = 0
    shadow_index = 0

    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        if "PokemonIndex" in data["Metadata"]:
            self.pokemon_index = data["Metadata"]["PokemonIndex"]
        self.shadow_index = data["Metadata"]["ShadowIndex"]
        super().__init__(player, address, parent, **data)

    def to_json(self):
        return {
            **super().to_json(),
            "PokemonIndex": self.pokemon_index,
            "ShadowIndex": self.shadow_index
        }

class PokemonXDPurifyPokemonLocation(PokemonXDLocation):
    pokemon_index = 0
    shadow_index = 0

    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        if "PokemonIndex" in data["Metadata"]:
            self.pokemon_index = data["Metadata"]["PokemonIndex"]
        self.shadow_index = data["Metadata"]["ShadowIndex"]
        super().__init__(player, address, parent, **data)

    def to_json(self):
        return {
            **super().to_json(),
            "PokemonIndex": self.pokemon_index,
            "ShadowIndex": self.shadow_index
        }

class PokemonXDTrainerBattleLocation(PokemonXDLocation):
    battle_index = 0

    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        self.battle_index = data["Metadata"]["BattleIndex"]
        super().__init__(player, address, parent, **data)

    def to_json(self):
        return {
            **super().to_json(),
            "BattleIndex": self.battle_index
        }


class PokemonXDGiftLocation(PokemonXDLocation):
    item_id: int = 0
    room_id: int = 0

    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        self.room_id = data["Metadata"]["RoomId"]
        self.item_id = data["Metadata"]["ItemIndex"]
        super().__init__(player, address, parent, **data)

    def to_json(self):
        return {
            **super().to_json(),
            "RoomIndex": self.room_id,
            "ItemIndex": self.item_id,
        }


class PokemonXDTreasureLocation(PokemonXDLocation):
    treasure_index: int = 0

    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        self.treasure_index = data["Metadata"]["TreasureIndex"]
        super().__init__(player, address, parent, **data)

    def to_json(self):
        return {
            **super().to_json(),
            "TreasureIndex": self.treasure_index,
        }


class PokemonXDTutorMoveLocation(PokemonXDLocation):
    tutor_move_index: int = 0

    def __init__(self, player: int, address: Optional[int], parent: Optional[Region], **data):
        self.tutor_move_index = data["Metadata"]["TutorMoveIndex"]
        super().__init__(player, address, parent, **data)

    def to_json(self):
        return {
            **super().to_json(),
            "TutorMoveIndex": self.tutor_move_index
        }
