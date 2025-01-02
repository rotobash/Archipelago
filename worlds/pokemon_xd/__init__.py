

import random
import settings
import typing
from .Items import PokemonXDItem, PokemonXDAPItem  # the options we defined earlier
from .Options import PokemonXDOptions  # the options we defined earlier
# from .items import mygame_items  # data used below to add items to the World
# from .locations import mygame_locations  # same as above
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Region, Location, Entrance, Item, ItemClassification, Tutorial
from worlds.generic.Rules import add_rule, set_rule, forbid_item, add_item_rule



class PokemonXDItem(Item):  # or from Items import MyGameItem
    game = "My Game"  # name of the game/world this item is from


class PokemonXDLocation(Location):  # or from Locations import MyGameLocation
    game = "My Game"  # name of the game/world this location is in


class PokemonXDSettings(settings.Group):
    class RomFile(settings.SNESRomPath):
        """Insert help text for host.yaml here."""

    rom_file: RomFile = RomFile("MyGame.sfc")


class PokemonXDWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up a Pokemon XD game integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["rotobash"]
    )]

class PokemonXDWorld(World):
    """Insert description of the world/game here."""
    game = "My Game"  # name of the game/world
    options_dataclass = PokemonXDOptions  # options the player can set
    options: PokemonXDOptions  # typing hints for option results
    settings: typing.ClassVar[PokemonXDSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    base_id = 1234
    # instead of dynamic numbering, IDs could be part of data

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = {} #{name: id for
                       #id, name in enumerate(mygame_items, base_id)}
    location_name_to_id = {} #{name: id for
                           #id, name in enumerate(mygame_locations, base_id)}

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = {
        "weapons": {"sword", "lance"},
    }

    def generate_early(self) -> None:
        return super().generate_early()
    
    def create_regions(self) -> None:
        return super().create_regions()