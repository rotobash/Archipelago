from dataclasses import dataclass
from enum import Enum
from Options import Option, DefaultOnToggle, PerGameCommonOptions, Range, Toggle, DeathLink, Choice, OptionSet
# from .randomizer_options.RandomizerOptions import RandomizerOptions

class PokemonItemOptionType(Enum):
    Snags = 1,
    Pokespots = 2,
    Gifts = 3

class TrainersanityOptionType(Enum):
    Story = 1,
    MtBattle = 2,
    Colosseum = 3,
    BattleCD = 4

class ItemChecks(DefaultOnToggle):
    """ """
    display_name = "Add Item Checks"

class PokemonAsItemsToggle(Toggle):
    """ Enables pokemon checks as items.  """

class PokemonAsItemsOptions(OptionSet):
    """  Pokemon will not be added to your party unless it has been sent by the server."""
    display_name = "Pokemon Are Items"
    valid_keys = [
        PokemonItemOptionType.Snags.name,
        PokemonItemOptionType.Pokespots.name,
        PokemonItemOptionType.Gifts.name
    ]
    default = valid_keys

class TrainersanityToggle(Toggle):
    """ Enables trainer battle checks.  """

class TrainersanityOptions(OptionSet):
    """ Battling trainers will unlock items. """
    display_name = "Add Battle Win Checks"
    valid_keys = [
        TrainersanityOptionType.Story.name,
        TrainersanityOptionType.MtBattle.name,
        TrainersanityOptionType.Colosseum.name
    ]
    default = [TrainersanityOptionType.Story.name]

class PurifyPokemon(Toggle):
    """ Purifying pokemon will unlock items. """
    display_name = "Add Purify Pokemon Checks"

@dataclass
class PokemonXDOptions(PerGameCommonOptions):
    item_checks: ItemChecks
    pokemon_as_items_toggle: PokemonAsItemsToggle
    pokemon_as_items: PokemonAsItemsOptions
    purify_pokemon: PurifyPokemon
    trainersanity_toggle: TrainersanityToggle
    trainersanity: TrainersanityOptions
    death_link: DeathLink
    # randomizer_options: RandomizerOptions