from core.database import Database


class TroopDatabase:
    def __init__(self):
        self.db = Database()

    def get(self, tier: str, troop_type: str):
        for troop in self.db.troops:
            if troop["tier"] == tier and troop["type"] == troop_type:
                return troop

        return None