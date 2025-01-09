import enum
import typing
from Options import Option, DefaultOnToggle, Range, Toggle, DeathLink, Choice, OptionSet

class PokemonItemOptionType(enum):
    OFF = 0,
    SNAGS = 1,
    POKESPOTS = 2,
    GIFTS = 3

class TrainersanityOptionType(enum):
    OFF = 0,
    STORY = 1,
    MTBATTLE = 2,
    COLO = 3,
    BATTLECD = 4

class ItemChecks(DefaultOnToggle):
    """ """
    display_name = "Add Item Checks"

class PokemonAsItems(OptionSet):
    """ Pokemon are treated as items. Pokemon will not be added to your party unless it has been sent by the server."""
    display_name = "Pokemon Are Items"
    options = {
        {"Snags", PokemonItemOptionType.SNAGS },
        {"PokeSpots", PokemonItemOptionType.POKESPOTS },
        {"Gifts", PokemonItemOptionType.GIFTS }
    }

class Trainersanity(OptionSet):
    """ Battling trainers will unlock items. """
    display_name = "Add Battle Win Checks"
    options = {
        {"Off", TrainersanityOptionType.OFF },
        {"Story Battles", TrainersanityOptionType.STORY},
        {"Mt. Battle", TrainersanityOptionType.MTBATTLE},
        {"Colosseum", TrainersanityOptionType.COLO},
        # {"Battle CDs", 0},
    }

class PurifyPokemon(Toggle):
    """ Purifying pokemon will unlock items. """
    display_name = "Add Purify Pokemon Checks"


xd_options: typing.Dict[str, typing.Type[Option]] = {
    { "ItemChecks", ItemChecks },
    { "PokemonAsItems", PokemonAsItems },
    { "PurifyPokemon", PurifyPokemon },
    { "Trainersanity", Trainersanity },
    { "death_link", DeathLink }
}