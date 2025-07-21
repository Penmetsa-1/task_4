# app.py
# Author: Sandeep Penmetsa
# Task 4: Build a REST API with Flask
# Internship: BrokiesHub - Python Developer Internship (pyInt)
# Description: A simple Flask-based REST API to manage user data

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
users = []

# Utility function to find user by ID
def find_user(user_id):
    return next((user for user in users if user['id'] == user_id), None)

# Route: Home
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the User Management API!"})

# Route: Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# Route: Get user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = find_user(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Route: Add new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or not all(key in data for key in ("id", "name", "email")):
        return jsonify({"error": "Invalid user data"}), 400

    if find_user(data["id"]):
        return jsonify({"error": "User with this ID already exists"}), 409

    users.append(data)
    return jsonify({"message": "User added successfully", "user": data}), 201

# Route: Update existing user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user.update({
        "name": data.get("name", user["name"]),
        "email": data.get("email", user["email"])
    })
    return jsonify({"message": "User updated successfully", "user": user})

# Route: Delete user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = find_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    users.remove(user)
    return jsonify({"message": "User deleted successfully"})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
