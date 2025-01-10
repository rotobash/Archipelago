import settings
import typing
from .Data import generate_story_events, generate_shadow_pokemon_lists, generate_treasure_list, generate_pokespot_pokemon_lists, generate_purify_pokemon_lists, generate_trainer_battle_lists
from .Options import xd_options, PokemonItemOptionType, TrainersanityOptionType
from .Regions import PokemonXDRegion, create_pokemonxd_regions
from worlds.AutoWorld import World

class PokemonXDSettings(settings.Group):
    class RomFile(settings.FilePath):
        """Insert help text for host.yaml here."""

    rom_file: RomFile = RomFile("Pokemon XD.iso")


class PokemonXDWorld(World):
    """Insert description of the world/game here."""
    game = "Pokemon XD"
    options_dataclass = xd_options
    settings: typing.ClassVar[PokemonXDSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler
    base_id = 0x47585800

    def create_regions(self):
        create_pokemonxd_regions(self.player, self.multiworld)
    

    def generate_basic(self):
        region_to_location_list = { region_id:[] for region_id in range(15)}
        regions: list[PokemonXDRegion] = self.multiworld.get_regions(self.player)

        address = self.base_id

        if self.multiworld.ItemChecks[self.player].value:
            address += generate_treasure_list(self.player, address, region_to_location_list)

        pokemon_as_items = self.multiworld.PokemonAsItems[self.player].value
        if len(pokemon_as_items) > 0:
            if PokemonItemOptionType.POKESPOTS in pokemon_as_items:
                address += generate_pokespot_pokemon_lists(self.player, address, region_to_location_list)

            if PokemonItemOptionType.SNAGS in pokemon_as_items:
                address += generate_shadow_pokemon_lists(self.player, address, region_to_location_list)

        if self.multiworld.PurifyPokemon[self.player].value:
            address += generate_purify_pokemon_lists(self.player, address, region_to_location_list)

        trainer_sanity = self.multiworld.Trainersanity[self.player].value
        if trainer_sanity:
            address += generate_trainer_battle_lists(self.player, address, region_to_location_list)

        for region_id, locations in region_to_location_list:
            for region in regions:
                if region.area_id == 0:
                    pass
                if region.room_id == region_id:
                    region.locations.append(locations)

        
        

