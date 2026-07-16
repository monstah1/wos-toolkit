from pathlib import Path
import json

DATA_DIR = Path(__file__).parent.parent / "data"


def save(name, key):
    path = DATA_DIR / f"{name}.json"

    if not path.exists():
        with open(path, "w", encoding="utf-8") as f:
            json.dump({key: []}, f, indent=4)

    print(f"✓ {name}.json ready")


save("heroes", "heroes")
save("troops", "troops")
save("gear", "gear")
save("pets", "pets")
save("research", "research")