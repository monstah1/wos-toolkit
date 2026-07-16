from core.loader import load_json


class Database:

    def __init__(self):

        self.heroes = load_json("heroes.json")

        self.troops = load_json("troops.json")

        self.gear = load_json("gear.json")

        self.pets = load_json("pets.json")

        self.research = load_json("research.json")