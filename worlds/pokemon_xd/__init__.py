import settings
import typing

from .Items import PokemonXDItem
from .Locations import PokemonXDLocation
from .Data import generate_lists, generate_purify_pokemon_lists, generate_pokespot_pokemon_lists, generate_shadow_pokemon_lists, generate_trainer_battle_lists, generate_treasure_list
from .Options import PokemonXDOptions, PokemonItemOptionType, TrainersanityOptionType
from .Regions import PokemonXDRegion, create_pokemonxd_regions
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
    base_id = 0x47585800

    item_name_to_id = {}
    item_id_to_name = {}
    location_name_to_id = {}
    location_id_to_name = {}

    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)

        (locations, items) = generate_lists(player, self.base_id)
        self.item_id_to_name = { i.code:i.name for i in items }
        self.item_name_to_id = { i.name:i.code for i in items }
        self.location_id_to_name = { i.address:i.name for i in locations }
        self.location_name_to_id = { i.name:i.address for i in locations }

    def create_regions(self):
        create_pokemonxd_regions(self.player, self.multiworld)
    

    def generate_basic(self):
        regions: list[PokemonXDRegion] = self.multiworld.get_regions(self.player)
        locations: list[PokemonXDLocation] = []
        itmes: list[PokemonXDItem] = []

        if self.options.item_checks:
            (locs, its) = generate_treasure_list(self.player, self.base_id)
            locations.extend(locs)
            itmes.extend(its)

        pokemon_as_items = self.options.pokemon_as_items
        if self.options.pokemon_as_items_toggle:
            if PokemonItemOptionType.Pokespots.name in pokemon_as_items:
                (locs, its) = generate_pokespot_pokemon_lists()
                locations.extend(locs)
                itmes.extend(its)

            if PokemonItemOptionType.Snags.name in pokemon_as_items:
                (locs, its) = generate_shadow_pokemon_lists(self.player, self.base_id)
                locations.extend(locs)
                itmes.extend(its)

        if self.options.purify_pokemon:
            (locs, its) = generate_purify_pokemon_lists(self.player, self.base_id)
            locations.extend(locs)
            itmes.extend(its)

        if self.options.trainersanity_toggle:
            trainer_sanity = self.options.trainersanity
            (locs, its) = generate_trainer_battle_lists(self.player, self.base_id)
            locations.extend(locs)
            itmes.extend(its)

        self.multiworld.itempool += itmes

        
        

