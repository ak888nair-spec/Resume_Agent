import bcrypt
import json
from pathlib import Path

ADMIN_FILE = Path(__file__).parent.parent / "admins.json"


def load_admins():
    with open(ADMIN_FILE, "r") as file:
        return json.load(file)["admins"]


def verify_admin(username: str, password: str):

    admins = load_admins()

    for admin in admins:

        if admin["username"] == username:

            stored_hash = admin["password"].encode()

            if bcrypt.checkpw(password.encode(), stored_hash):
                return True

    return False
