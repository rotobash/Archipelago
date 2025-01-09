from BaseClasses import Item, ItemClassification


class PokemonXDItem(Item):
    game: str = "Pokemon XD"
    quantity: int = 1
    name: str = ""

    def __init__(self, code, player: int, **data):
        flag = 0
        self.quantity = data["Quantity"]
        self.name = data["Name"]
        item_classifications: list[str] = data["ItemClassifications"]

        for cls in item_classifications:
            if cls.lower() == ItemClassification.progression.name:
                flag &= ItemClassification.progression
            elif cls.lower() == ItemClassification.useful.name:
                flag &= ItemClassification.useful
            elif cls.lower() == ItemClassification.filler.name:
                flag &= ItemClassification.filler

        super.__init__(self, self.name, flag, code, player)


class PokemonXDPokemonItem(PokemonXDItem):
    pokemon_index = 0