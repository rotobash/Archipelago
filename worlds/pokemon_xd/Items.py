from enum import Enum
from typing import Optional
from BaseClasses import Item, ItemClassification

POKEMON_XD_REMOTE_ITEM = 81
POKEMON_XD_POKEMON_ITEM = 83
POKEMON_XD_MONEY_ITEM = 84
POKEMON_XD_PURIFY_ITEM = 85
POKEMON_XD_TUTORMOVE_ITEM = 86


class PokemonItemType(Enum):
    EVENT = 0,
    ITEM = 1,
    POKEMON = 2,
    MONEY = 3,
    PURIFY = 4,
    TUTORMOVE = 5


class PokemonXDStoryEvent(Item):
    story_flag_id = 0

    def __init__(self, player, **data):
        name = data["Name"]
        self.story_flag_id = data["StoryFlagId"]
        super().__init__(name, ItemClassification.useful, None, player)

class PokemonXDItem(Item):
    game: str = "Pokemon XD"
    quantity: int = 1
    name: str = ""
    item_type: PokemonItemType = PokemonItemType.EVENT
    index: int = 0

    def __init__(self, code: Optional[int], player: int, **data):
        flag = 0
        self.quantity = data["Metadata"]["Quantity"]
        self.name = data["Name"]
        self.index = data["Index"]
        item_classifications: list[str] = data["ItemClassification"]

        flags = 0
        for cls in item_classifications:
            cls = cls.lower()
            if cls == ItemClassification.progression.name:
                flags |= ItemClassification.progression
            elif cls == ItemClassification.useful.name:
                flags |= ItemClassification.useful
            elif cls == ItemClassification.filler.name:
                flags |= ItemClassification.filler

        super().__init__(self.name, ItemClassification(flags), code + data["Index"], player)

    def to_json(self):
        return {
            "Name": self.name,
            "Index": self.index,
            "Quantity": self.quantity,
            "ItemClassification": [cls.name for cls in self.classification],
            "ItemType": self.item_type.name
        }


class PokemonXDPokemonItem(PokemonXDItem):
    pokemon_index = 0
    shadow_index = 0
    item_type = PokemonItemType.POKEMON

    def __init__(self, code: Optional[int], player: int, **data):
        self.pokemon_index = data["Metadata"]["PokemonIndex"]
        if "ShadowIndex" in data["Metadata"]:
            self.shadow_index = data["Metadata"]["ShadowIndex"]
        super().__init__(code, player, **data)

    def to_json(self):
        return {
            **super().to_json(),
            "PokemonIndex": self.pokemon_index,
            "ShadowIndex": self.shadow_index
        }


class PokemonXDMoneyItem(PokemonXDItem):
    battle_index = 0
    # quantity is amount of money
    item_type = PokemonItemType.MONEY
    def __init__(self, code, player, **data):
        self.battle_index = data["Metadata"]["BattleIndex"]
        super().__init__(code, player, **data)

    def to_json(self):
        return {
            **super().to_json(),
            "BattleIndex": self.battle_index
        }

class PokemonXDPurifyPokemonItem(PokemonXDItem):
    item_type = PokemonItemType.PURIFY
    item_index = 0

    def __init__(self, code: Optional[int], player: int, **data):
        self.item_index = data["Metadata"]["ItemIndex"]
        super().__init__(code, player, **data)

    def to_json(self):
        return {
            **super().to_json(),
            "ItemIndex": self.item_index
        }

class PokemonXDFoundItem(PokemonXDItem):
    item_index = 0
    item_type = PokemonItemType.ITEM
    
    def __init__(self, code: Optional[int], player: int, **data):
        self.item_index = data["Metadata"]["ItemIndex"]
        super().__init__(code, player, **data)

    def to_json(self):
        return {
            **super().to_json(),
            "ItemIndex": self.item_index
        }

class PokemonXDTutorMoveItem(PokemonXDItem):  
    move_index = 0
    item_type = PokemonItemType.TUTORMOVE  
    def __init__(self, code: Optional[int], player: int, **data):
        self.item_index = data["Metadata"]["TutorMoveIndex"]
        super().__init__(code, player, **data)

    def to_json(self):
        return {
            **super().to_json(),
            "TutorMoveIndex": self.move_index
        }