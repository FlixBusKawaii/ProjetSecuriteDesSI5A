# handlers/auth_handler.py
from flask import jsonify, request
from ..services.auth_service import AuthService

class AuthHandler:

    @staticmethod
    def register():
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        # Validation de base des données
        if not username or not password:
            return jsonify({"error": "Username and password are required"}), 400

        # Enregistrement de l'utilisateur
        user = AuthService.register_user(username, password)
        return jsonify({"message": "User registered successfully", "user": user.to_dict()}), 201

    @staticmethod
    def login():
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        # Vérification de l'utilisateur
        user = AuthService.verify_user(username, password)
        if user:
            return jsonify({"message": "Login successful", "user": user.to_dict()}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
