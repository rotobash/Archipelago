import json
import pkgutil

from .Locations import PokemonXDGiftLocation, PokemonXDPurifyPokemonLocation, PokemonXDTreasureLocation, PokemonXDLocation, PokemonXDPokemonLocation, PokemonXDTrainerBattleLocation, PokemonXDTutorMoveLocation
from .Items import PokemonXDItem, PokemonXDFoundItem, PokemonXDMoneyItem, PokemonXDPokemonItem, PokemonXDPurifyPokemonItem, PokemonXDTutorMoveItem

WORLD_DEFINITION_FILE = "xd.worlddef.json"
BASE_ID = 0x5858

def load_data_def(filename):
    data = pkgutil.get_data(__name__, "data/" + filename).decode("utf-8-sig")
    return json.loads(data)

def generate_location_name_to_id() -> dict[str, int]:
    """Generate dictionaries for location names to their IDs."""
    world_def = load_data_def(WORLD_DEFINITION_FILE)
    location_name_to_id = {location["Name"]: location["Index"] + BASE_ID for location in world_def["Locations"]}
    return location_name_to_id

def generate_item_name_to_id() -> dict[str, int]:
    """Generate dictionaries for item names to their IDs."""
    world_def = load_data_def(WORLD_DEFINITION_FILE)
    item_name_to_id = {f'{item["Name"]} ({item["Index"]})': item["Index"] + BASE_ID for item in world_def["Items"]}
    return item_name_to_id

def generate_lists(player: int) -> tuple[list[PokemonXDLocation], list[PokemonXDItem]]:
    locations = []
    items = []

    world_def = load_data_def(WORLD_DEFINITION_FILE)

    for item, location in zip(world_def["Items"], world_def["Locations"]):
        metadata = item["Metadata"]
        if metadata["Category"] == "Treasure":
            items.append(PokemonXDFoundItem(BASE_ID, player, **item))
            locations.append(PokemonXDTreasureLocation(player, BASE_ID, None, **location))
        elif metadata["Category"] == "NPC Gift":
            items.append(PokemonXDFoundItem(BASE_ID, player, **item))
            locations.append(PokemonXDGiftLocation(player, BASE_ID, None, **location))
        elif metadata["Category"] == "Shadow Snag" or metadata["Category"] == "Poke Spot":
            items.append(PokemonXDPokemonItem(BASE_ID, player, **item))
            locations.append(PokemonXDPokemonLocation(player, BASE_ID, None, **location))
        elif metadata["Category"] == "Shadow Purify":
            items.append(PokemonXDPurifyPokemonItem(BASE_ID, player, **item))
            locations.append(PokemonXDPurifyPokemonLocation(player, BASE_ID, None, **location))
        elif metadata["Category"] == "Trainer Battle":
            items.append(PokemonXDMoneyItem(BASE_ID, player, **item))
            locations.append(PokemonXDTrainerBattleLocation(player, BASE_ID, None, **location))
        elif metadata["Category"] == "Tutor Move":
            items.append(PokemonXDTutorMoveItem(BASE_ID, player, **item))
            locations.append(PokemonXDTutorMoveLocation(player, BASE_ID, None, **location))

    return (locations, items)
