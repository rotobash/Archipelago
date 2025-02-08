from functools import reduce
from typing import Collection
from BaseClasses import MultiWorld
from worlds.generic.Rules import add_rule, add_item_rule
from .Regions import PokemonXDRegion

GATEON_PORT_ENTRANCE_ROOM_ID = 153

def build_access_rules(player: int, multiworld: MultiWorld):
    regions: Collection[PokemonXDRegion] = multiworld.get_regions(player)
    purify_locations = filter(lambda f: "Purify" in f.name, multiworld.get_locations(player))
    
    # Krane is kidnapped, afterwards you are sent to Gateon port. you are forced to capture this teddiursa before progressing
    add_rule(multiworld.get_region("GATEON PORT - Exterior"), lambda state: multiworld.get_location("Capture NAPSs Shadow TEDDIURSA", player) in state.locations_checked)
    # after getting the Machine Part from Perr, you can return to HQ and get directed towards Agate
    add_rule(multiworld.get_region("AGATE VILLAGE - Exterior"), lambda state: state.has("MACHINE PART x 1", player))
    # at least one purified pokemon (does not matter which one) to get sent to talk to Vander at Mt. Battle
    add_rule(multiworld.get_region("MT BATTLE - Exterior"), lambda state: reduce(lambda x, y: x or y is not None, [l if l in state.locations_checked else None for l in purify_locations], False))
    # beat Vander to have him tell you about cipher lab
    add_rule(multiworld.get_region("CIPHER LAB - Exterior"), lambda state: multiworld.get_location("Defeat VANDER at MT. BATTLE (Round 10)", player) in state.locations_checked)
    
    # Krane wont let you leave cipher lab unless you actually *have* the data rom. make sure the player has it before or check that it is in cipher lab
    add_rule(multiworld.get_region("CIPHER LAB - Exterior"), lambda state: state.has("DATA ROM x 1", player) or "CIPHER LAB" in multiworld.find_item("DATA ROM x 1").area_name)
    
    # you are given back the Data Rom after Datan tries and fails to analyze it and sent to Pyrite town
    # add_rule(multiworld.get_region("PYRITE TOWN - Exterior"), lambda state: state.has("DATA ROM x 1", player))

    # 
    add_rule(multiworld.get_region("CIPHER LAB - Exterior"), lambda state: multiworld.get_location("Defeat VANDER at MT. BATTLE (Round 10)", player) in state.locations_checked)

    #


    


