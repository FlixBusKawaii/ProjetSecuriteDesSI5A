from flask import request, jsonify
from ..services.user_service import UserService
from ..utils.helpers import format_response, validate_email

class UserHandler:
    @staticmethod
    def create_user():
        data = request.get_json()
        username = data.get("username")

        # Validation basique
        if not username:
            return jsonify(format_response(False, message="Username is required")), 400

        # Appel au service pour créer un utilisateur
        new_user = UserService.create_user(username)
        if new_user:
            return jsonify(format_response(True, data={"user_id": new_user.id})), 201
        return jsonify(format_response(False, message="Failed to create user")), 500

    @staticmethod
    def get_user(user_id):
        user = UserService.get_user_by_id(user_id)
        if user:
            return jsonify(format_response(True, data={"username": user.username}))
        return jsonify(format_response(False, message="User not found")), 404

    @staticmethod
    def update_user(user_id):
        data = request.get_json()
        new_username = data.get("username")
        if not new_username:
            return jsonify(format_response(False, message="New username is required")), 400

        updated_user = UserService.update_username(user_id, new_username)
        if updated_user:
            return jsonify(format_response(True, data={"username": updated_user.username}))
        return jsonify(format_response(False, message="User not found")), 404

    @staticmethod
    def delete_user(user_id):
        if UserService.delete_user(user_id):
            return jsonify(format_response(True, message="User deleted"))
        return jsonify(format_response(False, message="User not found")), 404
