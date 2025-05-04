import json
import pkgutil

from .Locations import PokemonXDGiftLocation, PokemonXDTreasureLocation, PokemonXDLocation, PokemonXDPokemonLocation, PokemonXDTrainerBattleLocation, PokemonXDTutorMoveLocation
from .Items import PokemonXDItem, PokemonXDFoundItem, PokemonXDMoneyItem, PokemonXDPokemonItem, PokemonXDPurifyPokemonItem, PokemonXDTutorMoveItem

WORLD_DEFINITION_FILE = "xd.worlddef.json"

def load_data_def(filename):
    data = pkgutil.get_data(__name__, "data/" + filename).decode("utf-8-sig")
    return json.loads(data)


def generate_lists(player: int, base_id: int) -> tuple[list[PokemonXDLocation], list[PokemonXDItem]]:
    locations = []
    items = []

    world_def = load_data_def("xd.worlddef.json")

    for item, location in zip(world_def["Items"], world_def["Locations"]):
        metadata = item["Metadata"]
        if metadata["Category"] == "Treasure":
            items.append(PokemonXDFoundItem(base_id, player, **item))
            locations.append(PokemonXDTreasureLocation(player, base_id, None, **location))
        elif metadata["Category"] == "NPC Gift":
            items.append(PokemonXDFoundItem(base_id, player, **item))
            locations.append(PokemonXDGiftLocation(player, base_id, None, **location))
        elif metadata["Category"] == "Shadow Snag" or metadata["Category"] == "Poke Spot":
            items.append(PokemonXDPokemonItem(base_id, player, **item))
            locations.append(PokemonXDPokemonLocation(player, base_id, None, **location))
        elif metadata["Category"] == "Shadow Purify":
            items.append(PokemonXDPurifyPokemonItem(base_id, player, **item))
            locations.append(PokemonXDPokemonLocation(player, base_id, None, **location))
        elif metadata["Category"] == "Trainer Battle":
            items.append(PokemonXDMoneyItem(base_id, player, **item))
            locations.append(PokemonXDTrainerBattleLocation(player, base_id, None, **location))
        elif metadata["Category"] == "Tutor Move":
            items.append(PokemonXDTutorMoveItem(base_id, player, **item))
            locations.append(PokemonXDTutorMoveLocation(player, base_id, None, **location))

    return (locations, items)
