
import json

from BaseClasses import ItemClassification
from .Locations import PokemonXDItemLocation, PokemonXDLocation, PokemonXDPokespotPokemonLocation, PokemonXDShadowPokemonLocation, PokemonXDTrainerBattleLocation
from .Items import PokemonXDFoundItem, PokemonXDItem, PokemonXDMoneyItem, PokemonXDPokemonItem, PokemonXDPurifyPokemonItem


location_prefix = "data/locations/"
item_prefix = "data/items/"

def generate_treasure_list(player: int, base_id: int, region_to_location_list: dict[int, list]):
    give_locations_objs = json.loads(f"{location_prefix}treasure_items.json")
    give_item_objs = json.loads(f"{item_prefix}treasure_items.json")
    give_objs = zip(give_locations_objs, give_item_objs)

    offset = 0

    for give_obj in give_objs:
        (location_obj, item_obj) = give_obj
        location = PokemonXDItemLocation(player, base_id + offset, None, **location_obj)
        location.place_locked_item(PokemonXDFoundItem(base_id + offset, player, **item_obj))

        region_to_location_list[location.area_id].append(location)
        offset += 1

    return offset


def generate_shadow_pokemon_lists(player: int, base_id: int, region_to_location_list: dict[int, list]):
    offset = 0

    shadow_pokemon_locations_objs = json.loads(f"{location_prefix}shadow_pokemon.json")
    shadow_pokemon_item_objs = json.loads(f"{item_prefix}shadow_pokemon.json")
    pokemon_objs = zip(shadow_pokemon_locations_objs, shadow_pokemon_item_objs)

    for give_obj in pokemon_objs:
        (location_obj, item_obj) = give_obj
        location = PokemonXDShadowPokemonLocation(player, base_id + offset, None, **location_obj)
        location.place_locked_item(PokemonXDPokemonItem(base_id + offset, player, **item_obj))

        region_to_location_list[location.area_id].append(location)
        offset += 1

    return offset


def generate_pokespot_pokemon_lists(player: int, base_id: int, region_to_location_list: dict[int, list]):
    offset = 0

    pokespot_pokemon_locations_objs = json.loads(f"{location_prefix}pokespot_pokemon.json")
    pokespot_pokemon_item_objs = json.loads(f"{item_prefix}pokespot_pokemon.json")
    pokemon_objs = zip(pokespot_pokemon_locations_objs, pokespot_pokemon_item_objs)

    for give_obj in pokemon_objs:
        (location_obj, item_obj) = give_obj
        location = PokemonXDPokespotPokemonLocation(player, base_id + offset, None, **location_obj)
        location.place_locked_item(PokemonXDPokemonItem(base_id + offset, player, **item_obj))

        region_to_location_list[location.area_id].append(location)
        offset += 1

    return offset

def generate_trainer_battle_lists(player: int, base_id: int, region_to_location_list: dict[int, list]):
    offset = 0

    trainer_battle_locations_objs = json.loads(f"{location_prefix}trainers.json")
    trainer_battle_item_objs = json.loads(f"{item_prefix}trainers.json")
    pokemon_objs = zip(trainer_battle_locations_objs, trainer_battle_item_objs)

    for give_obj in pokemon_objs:
        (location_obj, item_obj) = give_obj
        location = PokemonXDTrainerBattleLocation(player, base_id + offset, None, **location_obj)
        location.place_locked_item(PokemonXDMoneyItem(base_id + offset, player, **item_obj))

        region_to_location_list[location.area_id].append(location)
        offset += 1

    return offset

def generate_purify_pokemon_lists(player: int, base_id: int, region_to_location_list: dict[int, list]):
    offset = 0

    purify_pokemon_locations_objs = json.loads(f"{location_prefix}purify_pokemon.json")
    purify_pokemon_item_objs = json.loads(f"{item_prefix}purify_pokemon.json")
    pokemon_objs = zip(purify_pokemon_locations_objs, purify_pokemon_item_objs)

    for give_obj in pokemon_objs:
        (location_obj, item_obj) = give_obj
        location = PokemonXDShadowPokemonLocation(player, base_id + offset, None, **location_obj)
        location.place_locked_item(PokemonXDPurifyPokemonItem(base_id + offset, player, **item_obj))

        region_to_location_list[location.area_id].append(location)
        offset += 1

    return offset