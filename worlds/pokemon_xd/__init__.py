from BaseClasses import ItemClassification
import settings
import typing

from .Items import PokemonItemType, PokemonXDItem
from .Data import generate_lists
from .Options import PokemonXDOptions, PokemonItemOptionType, TrainersanityOptionType
from .Regions import PokemonXDRegion, create_pokemonxd_regions
from .Rules import build_access_rules
from worlds.AutoWorld import World

class PokemonXDSettings(settings.Group):
    class RomFile(settings.FilePath):
        """Insert help text for host.yaml here."""

    rom_file: RomFile = RomFile("Pokemon XD.iso")


class PokemonXDWorld(World):
    """Insert description of the world/game here."""
    game = "Pokemon XD"
    options_dataclass = PokemonXDOptions
    options: PokemonXDOptions
    settings: typing.ClassVar[PokemonXDSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler
    base_id = 0x5858

    item_name_to_id = {}
    item_id_to_name = {}
    location_name_to_id = {}
    location_id_to_name = {}

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)

        (locations, items) = generate_lists(player, self.base_id)
        self.locations = { i.address:i for i in locations }
        self.items = { i.code:i for i in items }
        self.item_id_to_name = { i.code:i.name for i in items }
        self.item_name_to_id = { i.name:i.code for i in items }
        self.location_id_to_name = { i.address:i.name for i in locations }
        self.location_name_to_id = { i.name:i.address for i in locations }

    def create_regions(self):
        self.origin_region_name = create_pokemonxd_regions(self.player, self.multiworld)
    
    def create_item(self, name):
        for item in self.items.values():
            if item.name == name:
                return item
            
        return PokemonXDItem(self.base_id, self.player, { "Index": len(self.locations), "Name": name, "Quantity": 1, "ItemClassification": [ItemClassification.filler]})

    def create_items(self):
        items: list[PokemonXDItem] = []
        locked_items:  list[PokemonXDItem] = []
        ap_items = self.items.values()

        treasure_items = [i for i in filter(lambda it: it.item_type == PokemonItemType.ITEM, ap_items)]
        if self.options.item_checks:
            items.extend(treasure_items)
        else:
            locked_items.extend(treasure_items)

        pokemon_as_items = self.options.pokemon_as_items
        snag_pokemon = [ i for i in filter(lambda it: it.item_type == PokemonItemType.POKEMON and it.shadow_index > 0, ap_items)]
        pokespot_pokemon = [ i for i in filter(lambda it: it.item_type == PokemonItemType.POKEMON and it.shadow_index == 0, ap_items)]

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

        purify_pokemon = [ i for i in filter(lambda it: it.item_type == PokemonItemType.PURIFY, ap_items)]
        if self.options.purify_pokemon:
            items.extend(purify_pokemon)
        else:
            locked_items.extend(purify_pokemon)

        trainer_battles = [ i for i in filter(lambda it: it.item_type == PokemonItemType.MONEY, ap_items)]
        if self.options.trainersanity_toggle:
            trainer_sanity = self.options.trainersanity
            items.extend(trainer_battles)
        else:
            locked_items.extend(trainer_battles)

        self.multiworld.itempool += items
        for locked_item in locked_items:
            location = self.locations[locked_item.code]
            location.place_locked_item(locked_item)

    # def set_rules(self):
    #     build_access_rules(self.player, self.multiworld)

        
        

