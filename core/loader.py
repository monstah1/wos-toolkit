import json
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data"


def load_json(filename):
    path = DATA_PATH / filename

    if not path.exists():
        return {}

    with open(path, "r", encoding="utf8") as f:
        return json.load(f)