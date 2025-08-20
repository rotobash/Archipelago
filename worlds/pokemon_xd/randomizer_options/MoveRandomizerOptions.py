from Options import Option, Toggle

class RandomizeMoves(Toggle):
    """ Randomizes the moves of pokemon. """
    display_name = "Randomize Moves"

class LegalMovesOnly(Toggle):
    """ Allows only moves Pokemon learn through level-up, TM or Move Tutor. """
    display_name = "Randomize Moves"

class ShareMovesets(Toggle):
    """ All Pokemon will use the last 4 level up moves they learn. """
    display_name = "Randomize Moves"

class BanShadowMoves(Toggle):
    """ Disallow randomized moves from being Shadow moves. """
    display_name = "Randomize Moves"

class BanEarlyDragonRage(Toggle):
    """ Bans Drag Rage as a potential move until Level 20. """
    display_name = "Randomize Moves"

class PreferType(Toggle):
    """ Random moves will more likely be STAB moves. """
    display_name = "Randomize Moves"

class ForceFourMoves(Toggle):
    """ Force Pokemon to have four moves. May use random moves if there are none to pick from. """
    display_name = "Randomize Moves"

class MoveRandomizerOptions(Option):
    randomize_moves: RandomizeMoves
    legal_moves_only: LegalMovesOnly
    share_movesets: ShareMovesets
    ban_shadow_moves: BanShadowMoves
    ban_early_dragon_rage: BanEarlyDragonRage
    prefer_type: PreferType
    force_four_moves: ForceFourMoves
    display_name = "Move Randomizer Options"