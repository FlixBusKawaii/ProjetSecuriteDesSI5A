from flask import Blueprint
from ..handlers.auth_handler import AuthHandler  # Import du handler d'authentification

# Définition du blueprint pour les routes d'authentification
auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    return AuthHandler.register()

@auth_bp.route('/login', methods=['POST'])
def login():
    return AuthHandler.login()

@auth_bp.route('/logout', methods=['POST'])
def logout():
    return AuthHandler.logout()