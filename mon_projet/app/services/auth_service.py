# services/auth_service.py
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.auth import Auth  # Suppose que le modèle `Auth` se trouve dans models/auth.py
from ..extensions import db_auth

class AuthService:

    @staticmethod
    def register_user(username, password):
        hashed_password = generate_password_hash(password)
        new_user = Auth(username=username, hashed_password=hashed_password)
        db_auth.session.add(new_user)
        db_auth.session.commit()
        return new_user

    @staticmethod
    def verify_user(username, password):
        user = Auth.query.filter_by(username=username).first()
        if user and check_password_hash(user.hashed_password, password):
            return user
        return None
