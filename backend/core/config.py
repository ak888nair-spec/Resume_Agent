import json
from pathlib import Path

CONFIG_FILE = Path(__file__).resolve().parent.parent / "config.json"


def load_config():
    if not CONFIG_FILE.exists():
        with open(CONFIG_FILE, "w") as f:
            json.dump({"recruitment_open": False}, f, indent=4)

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)


def recruitment_status():
    return load_config()["recruitment_open"]


def set_recruitment(status: bool):
    config = load_config()
    config["recruitment_open"] = status
    save_config(config)