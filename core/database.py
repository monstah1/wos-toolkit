from core.loader import load_json


class Database:
    def __init__(self):
        self.heroes = load_json("heroes.json").get("heroes", [])
        self.troops = load_json("troops.json").get("troops", [])
        self.gear = load_json("gear.json").get("gear", [])
        self.pets = load_json("pets.json").get("pets", [])
        self.research = load_json("research.json").get("research", [])