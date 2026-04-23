# my_services.py

import random, string
from werkzeug.security import generate_password_hash


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)


class Person:
    def __init__(self, pin, is_used=False):
        self.pin = pin
        self.is_used = is_used

    def to_dict(self):
        return {
            "pin": self.pin,
            "is_used": self.is_used
        }


def generate_long_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


def fake_db(size=10):
    return [Person(generate_long_string(), False).to_dict() for _ in range(size)]


def get_valid_codes(db):
    # return UNUSED codes
    return [p["pin"] for p in db if not p["is_used"]]


def use_code(db, code):
    for person in db:
        if person["pin"] == code and not person["is_used"]:
            person["is_used"] = True
            return True
    return False