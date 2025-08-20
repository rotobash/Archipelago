

from dataclasses import dataclass
from enum import Enum
from Options import Option, DefaultOnToggle, PerGameCommonOptions, Range, Toggle, DeathLink, Choice, OptionSet


class StarterOptionType(Enum):
    Unchanged = 1
    Random = 3
    RandomThreeStage = 4
    RandomTwoStage = 5
    RandomSingleStage = 6

class StarterOptions(OptionSet):
    """ Choose the starter pokemon. """
    display_name = "Set Starter Pokemon"
    valid_keys = list(StarterOptionType.__members__.keys())
    default = [StarterOptionType.Unchanged.name]

class RandomizeTeams(Toggle):
    """ Randomizes the teams of trainers. """
    display_name = "Randomize Trainer Teams"

class UseSimilarBSTs(Toggle):
    """ Randomized Pokemon will have a similar BST to the one they're replacing. """
    display_name = "Enable Team Randomization"

class DontUseLegendaries(Toggle):
    """ Legendaries are banned from being selected. """
    display_name = "Enable Team Randomization"

class LegendaryToLegendary(Toggle):
    """ Only legendary pokemon can be randomized to other legendary pokemon. """
    display_name = "Legendary to Legendary"

class CatchRateRange(Range):
    """ Set the catch rate of randomized pokemon. """
    display_name = "Catch Rate"
    min_value = 0
    max_value = 255
    default = 45

class ForceFullyEvolved(Toggle):
    """ Teams will use fully evolved Pokemon by level 35. """
    display_name = "Force Fully Evolved Pokemon"

class RandomizeHeldItems(Toggle):
    """ Randomizes the held items of pokemon in team randomization. """
    display_name = "Randomize Held Items"

@dataclass
class TeamRandomizerOptions(Option):
    """ Options for the Pokemon XD team randomizer. """
    starter_options: StarterOptions
    use_similar_bsts: UseSimilarBSTs
    legendary_to_legendary: LegendaryToLegendary
    dont_use_legendaries: DontUseLegendaries
    catch_rate_range: CatchRateRange
    force_fully_evolved: ForceFullyEvolved
    randomize_held_items: RandomizeHeldItems
    team_randomizer_options: RandomizeTeams
    display_name = "Pokemon XD Team Randomizer Options"