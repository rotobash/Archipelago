from BaseClasses import ItemClassification, MultiWorld, Region, CollectionState
from worlds.generic.Rules import add_rule
import json

from  .Items import PokemonXDStoryEvent
from .Locations import PokemonXDLocation

def exit(state: CollectionState) -> bool:
    return True


class PokemonXDRegion(Region):
    game: str = "Pokemon XD"
    area_id: int = 0
    story_flag: str = ""
    starting: bool = False

    def __init__(self, player: int, multiworld: MultiWorld, hint = None, **data):
        self.area_id = data["AreaId"]
        self.room_id = data["StoryFlag"]
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

def generate_story_events(player: int):
    story_flags: list[dict] = json.loads("data/story_flags.json")
    events: list[PokemonXDLocation] = []
    prev_item: PokemonXDStoryEvent = None

    for story_flag in story_flags:
        story_flag_item = PokemonXDStoryEvent(player, **story_flag)
        story_flag_location = PokemonXDLocation(player, None, None, **story_flag)

        story_flag_location.place_locked_item(story_flag_item)

        if prev_item is not None:
            add_rule(story_flag_location, lambda state: state.has(prev_item.name))

        prev_item = story_flag_item
        events.append(story_flag_location)  
    
    return events

def create_pokemonxd_regions(player: int, multiworld: MultiWorld) -> list[PokemonXDArea]:
    areas_obj: list[dict] = json.loads("data/areas.json")
    rooms_obj: list[dict] = json.loads("data/rooms.json")

    hub_area: PokemonXDArea = PokemonXDArea(player, multiworld, None, **{"Name": "Menu", "Starting": True, "AreaId": 0})
    hub_area.locations += generate_story_events()

    areas = [hub_area]
    rooms: list[PokemonXDRegion] = []
    
    for room_obj in rooms_obj:
        rooms.append(PokemonXDRegion(player, multiworld, None, **room_obj))

    for area_obj in areas_obj:
        area = PokemonXDArea(player, multiworld, None, **area_obj)

        if not area.starting:
            hub_area.connect(area, area.name, lambda state: state.has(area.story_flag, player))
        else:
            hub_area.connect(area, area.name)

        for room in rooms:
            if room.area_id == area.area_id:
                area.connect(room, f"{area.name} - Subarea {room.room_id}", lambda state: state.has(room.story_flag))

        
        areas.append(area)

    
    multiworld.regions.append(hub_area)
