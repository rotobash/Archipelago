
from dataclasses import dataclass
import json
from Options import Option, Toggle
from .randomizer_options import TraitRandomizerOptions, MoveRandomizerOptions, TeamRandomizerOptions

class TurnOffMoveAnimations(Toggle):
    """ Turns off move animations to speed up battles. """
    display_name = "Turn Off Move Animations"

@dataclass
class RandomizerOptions(Option):
    """ Options for the Pokemon XD randomizer. """
    display_name = "Pokemon XD Randomizer Options"
    turn_off_move_animations: TurnOffMoveAnimations
    trait_randomizer_options: TraitRandomizerOptions
    move_randomizer_options: MoveRandomizerOptions
    team_randomizer_options: TeamRandomizerOptions
    

    def to_randomizer_json(self):
        """ Convert the options to a JSON format for the randomizer. """
        return json.dumps({})