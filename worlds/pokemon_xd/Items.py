from enum import Enum
from typing import Optional
from BaseClasses import Item, ItemClassification

class PokemonItemType(Enum):
    EVENT = 0,
    ITEM = 1,
    POKEMON = 2,
    MONEY = 3,
    PURIFY = 4

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

    def __init__(self, code: Optional[int], player: int, **data):
        flag = 0
        self.quantity = data["Quantity"]
        self.name = data["Name"]
        item_classifications: list[str] = data["ItemClassification"]

        for cls in item_classifications:
            cls = cls.lower()
            if cls == ItemClassification.progression.name:
                flag &= ItemClassification.progression
            elif cls == ItemClassification.useful.name:
                flag &= ItemClassification.useful
            elif cls == ItemClassification.filler.name:
                flag &= ItemClassification.filler

        super().__init__(self.name, flag, code + data["Index"], player)


class PokemonXDPokemonItem(PokemonXDItem):
    pokemon_index = 0
    item_type = PokemonItemType.POKEMON

class PokemonXDMoneyItem(PokemonXDItem):
    # quantity is amount of money
    item_type = PokemonItemType.MONEY

class PokemonXDPurifyPokemonItem(PokemonXDItem):
    item_type = PokemonItemType.PURIFY

    def __init__(self, code: Optional[int], player: int, **data):
        super().__init__(code, player, **data)

class PokemonXDFoundItem(PokemonXDItem):
    item_index = 0
    item_type = PokemonItemType.ITEM
    
    def __init__(self, code: Optional[int], player: int, **data):
        self.item_index = data["ItemIndex"]
        super().__init__(code, player, **data)