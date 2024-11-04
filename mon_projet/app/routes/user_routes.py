from flask import Blueprint
from ..handlers.user_handler import UserHandler  # Import du handler utilisateur

# Définition du blueprint pour les routes utilisateur
user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/', methods=['POST'])
def create_user():
    return UserHandler.create_user()

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return UserHandler.get_user(user_id)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return UserHandler.update_user(user_id)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return UserHandler.delete_user(user_id)
