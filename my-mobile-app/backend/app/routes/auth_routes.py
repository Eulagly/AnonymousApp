from flask import Blueprint, request, jsonify

auth_routes = Blueprint("auth", __name__)

# Mock user database (you would replace this with a real database)
users = []


@auth_routes.route("/signup", methods=["POST"])
def signup():
    data = request.json

    # Check if the user already exists
    existing_user = next((user for user in users if user["username"] == data["username"]), None)
    if existing_user:
        return jsonify({"error": "Username already exists"}), 400

    # Create a new user
    new_user = {
        "username": data["username"],
        "password": data["password"],
    }
    users.append(new_user)

    return jsonify({"message": "User registered successfully"}), 201


@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.json

    # Find the user
    user = next((user for user in users if user["username"] == data["username"]), None)
    if user and user["password"] == data["password"]:
        return jsonify({"message": "Login successful"}), 200

    return jsonify({"error": "Invalid credentials"}), 401
