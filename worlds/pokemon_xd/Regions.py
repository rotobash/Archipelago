from BaseClasses import Region, CollectionState
import json

def exit(state: CollectionState) -> bool:
    return True

class PokemonXDRegion(Region):
    game: str = "Pokemon XD"
    areaId: int = 0

    def __init__(self, hub_region: Region, player, multiworld, hint = None, **data):
        self.areaId = data["AreaId"]
        name = data["Name"]
        super().__init__(name, player, multiworld, hint)


        self.add_exits([hub_region.name], { hub_region.name, exit })


def create_pokemonxd_regions(player, multiworld) -> list[PokemonXDRegion]:
    regions_obj: list[dict] = json.loads("data/regions.json")
    hub_region: PokemonXDRegion = None
    regions = []

    for region_obj in regions_obj:
        if region_obj["Name"] == "HUB":
            hub_region = PokemonXDRegion(None, player, multiworld, None, **region_obj)
            continue

        region = PokemonXDRegion(hub_region, player, multiworld, None, **region_obj)
        regions.append(region)

    
    return regions
