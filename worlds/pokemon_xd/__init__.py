import json
import os
from BaseClasses import ItemClassification
import settings
import typing

from .Items import PokemonItemType, PokemonXDItem
from .Data import generate_lists
from .Options import PokemonXDOptions, PokemonItemOptionType, TrainersanityOptionType
from .Regions import create_pokemonxd_regions
from .Rules import build_access_rules
from worlds.AutoWorld import World

class PokemonXDSettings(settings.Group):
    class RomFile(settings.FilePath):
        """Insert help text for host.yaml here."""
    class DolphinPath(settings.FilePath):
        """Insert help text for host.yaml here."""

    rom_file: RomFile = RomFile("Pokemon XD.iso")
    dolphin_path: DolphinPath = DolphinPath("Dolphin.exe")


class PokemonXDWorld(World):
    """Insert description of the world/game here."""
    game = "Pokemon XD"
    options_dataclass = PokemonXDOptions
    options: PokemonXDOptions
    # will be automatically assigned from type hint
    settings: typing.ClassVar[PokemonXDSettings]
    topology_present = True  # show path to required location checks in spoiler
    base_id = 0x5858

    item_name_to_id = {}
    location_name_to_id = {}

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)

        (locations, items) = generate_lists(player, self.base_id)
        self.locations = {i.address: i for i in locations}
        self.locations_by_name = {i.name: i for i in locations}
        self.items = {i.code: i for i in items}

        self.item_name_to_id = {i.name: i.code for i in items}
        self.location_name_to_id = {i.name: i.address for i in locations}

    def create_regions(self):
        self.origin_region_name = create_pokemonxd_regions(
            self.player, self.multiworld, self.locations_by_name)

    def create_item(self, name):
        for item in self.items.values():
            if item.name == name:
                return item

        return PokemonXDItem(self.base_id, self.player, {"Index": len(self.locations) + self.base_id, "Name": name, "Quantity": 1, "ItemClassification": [ItemClassification.filler]})

    def create_items(self):
        items: list[PokemonXDItem] = []
        locked_items:  list[PokemonXDItem] = []
        ap_items = self.items.values()

        treasure_items = [i for i in filter(
            lambda it: it.item_type == PokemonItemType.ITEM, ap_items)]
        if self.options.item_checks:
            items.extend(treasure_items)
        else:
            locked_items.extend(treasure_items)

        pokemon_as_items = self.options.pokemon_as_items
        snag_pokemon = [i for i in filter(
            lambda it: it.item_type == PokemonItemType.POKEMON and it.shadow_index > 0, ap_items)]
        pokespot_pokemon = [i for i in filter(
            lambda it: it.item_type == PokemonItemType.POKEMON and it.shadow_index == 0, ap_items)]

        if self.options.pokemon_as_items_toggle:
            if PokemonItemOptionType.Pokespots.name in pokemon_as_items:
                items.extend(pokespot_pokemon)
            else:
                locked_items.extend(pokespot_pokemon)

            if PokemonItemOptionType.Snags.name in pokemon_as_items:
                items.extend(snag_pokemon)
            else:
                locked_items.extend(snag_pokemon)
        else:
            locked_items.extend(snag_pokemon)
            locked_items.extend(pokespot_pokemon)

        purify_pokemon = [i for i in filter(
            lambda it: it.item_type == PokemonItemType.PURIFY, ap_items)]
        
        if self.options.purify_pokemon:
            items.extend(purify_pokemon)
        else:
            locked_items.extend(purify_pokemon)

        trainer_battles = [i for i in filter(
            lambda it: it.item_type == PokemonItemType.MONEY, ap_items)]
        if self.options.trainersanity_toggle:
            trainer_sanity = self.options.trainersanity
            items.extend(trainer_battles)
        else:
            locked_items.extend(trainer_battles)

        tutor_moves = [i for i in filter(
            lambda it: it.item_type == PokemonItemType.TUTORMOVE, ap_items)]
        locked_items.extend(tutor_moves)

        self.multiworld.itempool += items
        for locked_item in locked_items:
            location = self.locations[locked_item.code]
            location.place_locked_item(locked_item)

    # def set_rules(self):
    #     build_access_rules(self.player, self.multiworld)

    def generate_output(self, output_directory):
        filled_location_info = []
        item_info = [i.to_json() for i in self.items.values()]

        for filled_location in self.multiworld.get_filled_locations(self.player):
            fill_item = {
                "APAddress": filled_location.address,
                "LocationData": filled_location.to_json()
            }

            filled_location_info.append(fill_item)

        options_dict = {
            "Game": self.game,
            "Seed": self.multiworld.seed_name,
            "Slot": self.multiworld.player_name[self.player],
            "DolphinPath": self.settings.dolphin_path,
            "RomFile": self.settings.rom_file,
            "BaseId": self.base_id,
            "OptionsFlag": 0xFFFF,
            "Locations": filled_location_info
        }

        # generate output path
        mod_name = self.multiworld.get_out_file_name_base(self.player)
        out_file = os.path.join(output_directory, mod_name + ".apxd")
        with open(out_file, "w") as outfile:
            json.dump(options_dict, outfile)
