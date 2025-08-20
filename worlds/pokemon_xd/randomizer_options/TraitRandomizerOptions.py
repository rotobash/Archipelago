
from dataclasses import dataclass
from enum import Enum
from Options import Option, DefaultOnToggle, OptionSet, Toggle

class MoveCompatibility(Enum):
    """ Defines the compatibility of moves with Pokemon. """
    Unchanged = 1
    Random = 2
    RandomPreferType = 3
    Full = 3

class TMCompatibility(OptionSet):
    """ Defines the compatibility of TMs with Pokemon. """
    display_name = "TM Compatibility"
    valid_keys = [move.name for move in MoveCompatibility]
    default = [MoveCompatibility.Unchanged.name]

class TutorMoveCompatibility(OptionSet):
    """ Defines the compatibility of Tutor moves with Pokemon. """
    display_name = "Tutor Move Compatibility"
    valid_keys = [move.name for move in MoveCompatibility]
    default = [MoveCompatibility.Unchanged.name]

class EasyEvolutions(DefaultOnToggle):
    """ All Pokemon reach their final form by level 40. """
    display_name = "Easy Evolutions"

class FixImpossibleEvolutions(Toggle):
    """ Makes it easier to evolve Pokemon by removing impossible requirements. """
    display_name = "Fix Impossible Evolutions"

class AbilityRandomizerToggle(Toggle):
    """ Randomizes the abilities of pokemon. """
    display_name = "Randomize Abilities"

class BanBadAbilities(DefaultOnToggle):
    """ Bans abilities that are considered bad or game-breaking. """
    display_name = "Ban Bad Abilities"

class AllowWonderGuard(Toggle):
    """ Allows the Wonder Guard ability to be randomized. """
    display_name = "Allow Wonder Guard"


@dataclass
class TraitRandomizerOptions(Option):
    """ Options for the Pokemon XD trait randomizer. """
    display_name = "Trait Randomizer Options"
    tm_compatibility: TMCompatibility
    tutor_move_compatibility: TutorMoveCompatibility
    easy_evolutions: EasyEvolutions
    fix_impossible_evolutions: FixImpossibleEvolutions
    ability_randomizer_toggle: AbilityRandomizerToggle
    ban_bad_abilities: BanBadAbilities
    allow_wonder_guard: AllowWonderGuard