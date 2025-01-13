from BaseClasses import MultiWorld, Region, CollectionState
from worlds.generic.Rules import add_rule
from .json import load_region_json

from  .Items import PokemonXDStoryEvent
from .Locations import PokemonXDLocation

def exit(state: CollectionState) -> bool:
    return True


class PokemonXDRegion(Region):
    game: str = "Pokemon XD"
    room_id: int = 0
    area_name: str = ""
    requires: str = ""
    connects_to: list[int] = []
    starting: bool = False

    def __init__(self, player: int, multiworld: MultiWorld, hint = None, **data):
        self.room_id = data["RoomIndex"]
        self.area_name = data["AreaName"]
        self.starting = data["Starting"]
        self.requires = data["Requires"]
        self.connects_to = data["ConnectsTo"]
        name = data["Name"]
        super().__init__(name, player, multiworld, hint)

class PokemonXDArea(PokemonXDRegion):
    starting: bool = False

    def __init__(self, player: int, multiworld: MultiWorld, hint = None, **data):
        self.starting = data["Starting"]
        super().__init__(player, multiworld, hint, **data)

class PokemonXDRoom(PokemonXDRegion):
    room_id: int = 0
    def __init__(self, player, multiworld, hint=None, **data):
        self.room_id = data["RoomId"]
        super().__init__(player, multiworld, hint, **data)

# def generate_story_events(player: int):
#     story_flags: list[dict] = json.loads("data/story_flags.json")
#     events: list[PokemonXDLocation] = []
#     prev_item: PokemonXDStoryEvent = None

#     for story_flag in story_flags:
#         story_flag_item = PokemonXDStoryEvent(player, **story_flag)
#         story_flag_location = PokemonXDLocation(player, None, None, **story_flag)

#         story_flag_location.place_locked_item(story_flag_item)

#         if prev_item is not None:
#             add_rule(story_flag_location, lambda state: state.has(prev_item.name))

#         prev_item = story_flag_item
#         events.append(story_flag_location)  
    
#     return events

def create_pokemonxd_regions(player: int, multiworld: MultiWorld) -> list[PokemonXDArea]:
    # areas_obj: list[dict] = json.loads("data/areas.json")
    rooms_obj: list[dict] = load_region_json("regions.json")

    hub_area: PokemonXDRegion = PokemonXDRegion(player, multiworld, None, **{"Name": "Menu", "Starting": True, "AreaName": "HUB", "RoomIndex": 0, "Requires": None, "ConnectsTo": []})
    # hub_area.locations += generate_story_events()

    rooms: dict[str, list[PokemonXDRegion]] = {}
    
    for room_obj in rooms_obj:
        room = PokemonXDRegion(player, multiworld, None, **room_obj)
        if not room.area_name in rooms:
            rooms[room.area_name] = []

        rooms[room.area_name].append(room)

    for area in rooms.values():
        for room in area:
            multiworld.regions.append(room)

    
    multiworld.regions.append(hub_area)
