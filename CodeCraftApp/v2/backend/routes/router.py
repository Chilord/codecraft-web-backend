from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
import time

from ..services.my_services import fake_db, use_code
from ..services.storage import load_data, save_data, USERS_FILE, CODES_FILE
from ..services.meeting_links import *

auth_bp = Blueprint("auth", __name__)

# ------------------------
# LOAD PERSISTENT DATA
# ------------------------

users = load_data(USERS_FILE, {})  # { username: { password, paid_until } }
codes_db = load_data(CODES_FILE, fake_db(10))

save_data(CODES_FILE, codes_db)

print("Loaded users:", users)
print("Loaded codes:", codes_db)


# ------------------------
# ACCESS CHECK
# ------------------------

def is_access_valid(username):
    user = users.get(username)
    if not user:
        return False

    paid_until = user.get("paid_until", 0)
    return time.time() < paid_until


# ------------------------
# REGISTER
# ------------------------

@auth_bp.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")
    code = data.get("code")

    if not username or not password or not code:
        return jsonify({"message": "Missing fields"}), 400

    if username in users:
        return jsonify({"message": "User already exists"}), 400

    if not use_code(codes_db, code):
        return jsonify({"message": "Invalid or used code"}), 403

    users[username] = {
        "password": generate_password_hash(password),
        "paid_until": 0  # default: no access yet
    }

    save_data(USERS_FILE, users)
    save_data(CODES_FILE, codes_db)

    return jsonify({"message": "Account created successfully"}), 201


# ------------------------
# LOGIN
# ------------------------

@auth_bp.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    if not check_password_hash(user["password"], password):
        return jsonify({"message": "Invalid credentials"}), 401

    session["user"] = username

    return jsonify({
        "message": "Logged in",
        "access": is_access_valid(username)
    })


# ------------------------
# CURRENT USER
# ------------------------

@auth_bp.route("/api/me", methods=["GET"])
def me():
    username = session.get("user")

    if not username:
        return jsonify({"message": "Not logged in"}), 401

    user = users.get(username)

    return jsonify({
        "username": username,
        "has_access": is_access_valid(username),
        "paid_until": user.get("paid_until", 0)
    })


# ------------------------
# EXTEND ACCESS (FAKE PAYMENT HOOK)
# ------------------------

@auth_bp.route("/api/extend", methods=["POST"])
def extend_access():
    username = session.get("user")

    if not username:
        return jsonify({"message": "Not logged in"}), 401

    data = request.get_json()
    days = int(data.get("days", 30))

    now = time.time()
    current = users[username].get("paid_until", 0)

    base = max(now, current)
    users[username]["paid_until"] = base + days * 86400

    save_data(USERS_FILE, users)

    return jsonify({
        "message": "Access extended",
        "paid_until": users[username]["paid_until"]
    })


# ------------------------
# LOGOUT
# ------------------------

@auth_bp.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out"})


# ------------------------
# DEBUG
# ------------------------

@auth_bp.route("/api/debug", methods=["GET"])
def debug():
    return jsonify({
        "users": users,
        "codes": codes_db
    })

@auth_bp.route("/api/watch/<int:week>", methods=["GET", "POST"])
def get_video_link(week):
    if type(week) == "str":
        week = int(week)
    username = session.get("user")
    if not username:
        return jsonify({"error": "Not logged in"}), 401
    return jsonify({
        "video_embed": MEETING_LINKS[week]
    })