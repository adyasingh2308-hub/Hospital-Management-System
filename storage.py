import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def load_data(filename):
    """Load a list of records from a JSON file."""
    path = BASE_DIR / filename
    if not path.exists():
        save_data(filename, [])
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print(f"Warning: Could not read {filename}. Starting with an empty list.")
        return []


def save_data(filename, data):
    """Save records to a JSON file."""
    path = BASE_DIR / filename
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)