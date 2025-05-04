

from BaseClasses import MultiWorld, Region
from .Locations import PokemonXDLocation
from .Data import load_data_def

class PokemonXDRegion(Region):
    game: str = "Pokemon XD"
    room_id: int = 0
    requires: str = ""
    connects_to: dict[str, list] = []
    starting: bool = False
    map_entrance: bool = False

    def __init__(self, player: int, multiworld: MultiWorld, hint = None, **data):
        self.room_id = data["RoomIndex"]
        self.starting = data["Starting"]
        self.connects_to = data["ConnectsTo"]
        name = data["Name"]
        self.map_entrance = "Entrance" in name
        super().__init__(name, player, multiworld, hint)

    def as_json(self):
        return {
            "RoomIndex": self.room_id,
            "Starting": self.starting,
            "MapEntrance": self.map_entrance,
            "Requires": self.requires,
            "ConnectsTo": self.connects_to,
            "Name": self.name
        }

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

def create_pokemonxd_regions(player: int, multiworld: MultiWorld, locations: dict[str, PokemonXDLocation]):
    world_def = load_data_def("xd.worlddef.json")

    room_dict: dict[int, PokemonXDRegion] = {}
    hub_area: PokemonXDRegion = PokemonXDRegion(player, multiworld, None, **{"RoomIndex": 0, "Name": "Menu", "Starting": False, "ConnectsTo": {}, "Locations": {}})
    
    for room_obj in world_def["Regions"]:
        if room_obj["Unused"]:
            continue

        room = PokemonXDRegion(player, multiworld, None, **room_obj)
        room_dict[room.room_id] = room

        location_dict: dict[str, list] = room_obj["Locations"]
        for location_name in location_dict.keys():
            location = locations.get(location_name)
            room.locations.append(location)

        multiworld.regions.append(room)

    for room in room_dict.values():
        if room.map_entrance:
            entrance = room
            hub_area.connect(entrance)
            entrance.connect(hub_area)
            
        for room_id_str, access_rules in room.connects_to.items():
            room_connection = int(room_id_str)
            region = room_dict[room_connection]
            room.connect(region)

        for location in room.locations:
            location.parent_region = room



    return room_dict[141].name