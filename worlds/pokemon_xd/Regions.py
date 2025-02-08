

from BaseClasses import MultiWorld, Region
from .load_json import load_region_json


class PokemonXDRegion(Region):
    game: str = "Pokemon XD"
    room_id: int = 0
    area_name: str = ""
    requires: str = ""
    connects_to: list[int] = []
    starting: bool = False
    map_entrance: bool = False

    def __init__(self, player: int, multiworld: MultiWorld, hint = None, **data):
        self.room_id = data["RoomIndex"]
        self.area_name = data["AreaName"]
        self.starting = data["Starting"]
        self.map_entrance = data["Starting"]
        self.requires = data["Requires"]
        self.connects_to = data["ConnectsTo"]
        name = data["Name"]
        super().__init__(name, player, multiworld, hint)

    def as_json(self):
        return {
            "RoomIndex": self.room_id,
            "AreaName": self.area_name,
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

def create_pokemonxd_regions(player: int, multiworld: MultiWorld):
    # areas_obj: list[dict] = json.loads("data/areas.json")
    rooms_obj: list[dict] = load_region_json("regions.json")
    # hub_area.locations += generate_story_events()

    rooms: dict[str, list[PokemonXDRegion]] = {}
    room_dict: dict[int, PokemonXDRegion] = {}
    hub_area: PokemonXDRegion = None
    
    for room_obj in rooms_obj:
        room = PokemonXDRegion(player, multiworld, None, **room_obj)
        if not room.area_name in rooms:
            rooms[room.area_name] = []

        rooms[room.area_name].append(room)
        room_dict[room.room_id] = room

        if room.area_name == "HUB":
            hub_area = room

    for location in multiworld.get_locations(player):
        region = room_dict[location.room_id]
        location.parent_region = region
        region.locations.append(location)

    for area in rooms.values():
        for room in area:
            if room.map_entrance:
                entrance = room
                hub_area.connect(entrance)
                break

        for room in area:
            if not room.map_entrance:
                entrance.connect(room)
            multiworld.regions.append(room)

    

    # multiworld.regions.append(hub_area)

    return room_dict[141].name