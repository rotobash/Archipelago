from .load_json import load_check_json
from .Locations import PokemonXDItemLocation, PokemonXDLocation, PokemonXDPokemonLocation, PokemonXDTrainerBattleLocation
from .Items import PokemonXDItem, PokemonXDFoundItem, PokemonXDMoneyItem, PokemonXDPokemonItem, PokemonXDPurifyPokemonItem


def generate_lists(player: int, base_id: int) -> tuple[list[PokemonXDLocation], list[PokemonXDItem]]:
    locations = []
    items = []
    
    (location_list, item_list) = generate_treasure_list(player, base_id)
    locations.extend(location_list)
    items.extend(item_list)

    (location_list, item_list) = generate_shadow_pokemon_lists(player, base_id)
    locations.extend(location_list)
    items.extend(item_list)

    (location_list, item_list) = generate_pokespot_pokemon_lists(player, base_id)
    locations.extend(location_list)
    items.extend(item_list)

    (location_list, item_list) = generate_trainer_battle_lists(player, base_id)
    locations.extend(location_list)
    items.extend(item_list)

    (location_list, item_list) = generate_purify_pokemon_lists(player, base_id)
    locations.extend(location_list)
    items.extend(item_list)

    return (locations, items)

def generate_treasure_list(player: int, base_id: int):
    give_locations_objs = load_check_json(True, "treasure_items.json")
    give_item_objs = load_check_json(False, "treasure_items.json")
    give_objs = zip(give_locations_objs, give_item_objs)

    location_list: list[PokemonXDLocation] = []
    item_list: list[PokemonXDItem] = []

    for give_obj in give_objs:
        (location_obj, item_obj) = give_obj
        location_list.append(PokemonXDItemLocation(player, base_id, None, **location_obj))
        item_list.append(PokemonXDFoundItem(base_id, player, **item_obj))

    return (location_list, item_list)


def generate_shadow_pokemon_lists(player: int, base_id: int):
    shadow_pokemon_locations_objs = load_check_json(True, "shadow_pokemon.json")
    shadow_pokemon_item_objs = load_check_json(False, "shadow_pokemon.json")
    pokemon_objs = zip(shadow_pokemon_locations_objs, shadow_pokemon_item_objs)

    location_list = []
    item_list = []

    for give_obj in pokemon_objs:
        (location_obj, item_obj) = give_obj
        location_list.append(PokemonXDPokemonLocation(player, base_id, None, **location_obj))
        item_list.append(PokemonXDPokemonItem(base_id, player, **item_obj))

    return (location_list, item_list)


def generate_pokespot_pokemon_lists(player: int, base_id: int):
    pokespot_pokemon_locations_objs = load_check_json(True, "pokespot_pokemon.json")
    pokespot_pokemon_item_objs = load_check_json(False, "pokespot_pokemon.json")
    pokemon_objs = zip(pokespot_pokemon_locations_objs, pokespot_pokemon_item_objs)

    location_list = []
    item_list = []

    for give_obj in pokemon_objs:
        (location_obj, item_obj) = give_obj
        location_list.append(PokemonXDPokemonLocation(player, base_id, None, **location_obj))
        item_list.append(PokemonXDPokemonItem(base_id, player, **item_obj))

    return (location_list, item_list)

def generate_trainer_battle_lists(player: int, base_id: int):
    trainer_battle_locations_objs = load_check_json(True, "trainers.json")
    trainer_battle_item_objs = load_check_json(False, "trainers.json")
    pokemon_objs = zip(trainer_battle_locations_objs, trainer_battle_item_objs)

    location_list = []
    item_list = []

    for give_obj in pokemon_objs:
        (location_obj, item_obj) = give_obj
        location_list.append(PokemonXDTrainerBattleLocation(player, base_id, None, **location_obj))
        item_list.append(PokemonXDMoneyItem(base_id, player, **item_obj))

    return (location_list, item_list)

def generate_purify_pokemon_lists(player: int, base_id: int):
    purify_pokemon_locations_objs = load_check_json(True, "purify_pokemon.json")
    purify_pokemon_item_objs = load_check_json(False, "purify_pokemon.json")
    pokemon_objs = zip(purify_pokemon_locations_objs, purify_pokemon_item_objs)

    location_list = []
    item_list = []

    for give_obj in pokemon_objs:
        (location_obj, item_obj) = give_obj
        location_list.append(PokemonXDPokemonLocation(player, base_id, None, **location_obj))
        item_list.append(PokemonXDPurifyPokemonItem(base_id, player, **item_obj))

    return (location_list, item_list)